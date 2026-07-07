import os
import sys
import struct
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ─── 常量 ──────────────────────────────────────────────────
BMP_FOOTER_MAGIC = b'HYBR'

# ─── 加载私钥 ──────────────────────────────────────────────

def load_private_key(path):
    """从 PEM 文件加载 RSA 私钥"""
    if not os.path.exists(path):
        print(f"❌ 找不到私钥文件: {path}")
        print(f"   请先运行: python hybrid_encrypt.py --gen-key")
        print(f"   或指定路径: python hybrid_decrypt.py <文件> --key <私钥路径>")
        sys.exit(1)
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

# ─── 检测文件格式 ──────────────────────────────────────────

def is_encrypted_bmp(data):
    """检查是否为加密的 BMP（文件末尾有 HYBR 魔数）"""
    return len(data) >= 4 and data[-4:] == BMP_FOOTER_MAGIC

def parse_bmp_footer(data):
    """
    从加密 BMP 文件末尾解析元数据。
    尾部格式: [encrypted_key][nonce:12B][original_pixel_len:4B BE][key_len:4B BE][magic:4B]

    返回: (encrypted_key, nonce, original_pixel_len, bmp_header, encrypted_pixels)
    """
    magic = data[-4:]
    if magic != BMP_FOOTER_MAGIC:
        raise ValueError("不是加密的 BMP 文件（缺少 HYBR 尾标）")

    # 从文件末尾反向解析（固定偏移，干净无歧义）
    key_len = struct.unpack(">I", data[-8:-4])[0]
    original_pixel_len = struct.unpack(">I", data[-12:-8])[0]
    nonce = data[-24:-12]
    encrypted_key = data[-24 - key_len : -24]

    # 读取 BMP 文件头：偏移 10 处的 bfOffBits 告诉我们像素数据从哪里开始
    bfOffBits = struct.unpack_from("<I", data, 10)[0]
    header = data[:bfOffBits]

    # 加密的像素数据 = header 之后、元数据之前
    footer_start = len(data) - (key_len + 12 + 4 + 4 + 4)  # enc_key + nonce + orig_len + key_len + magic
    encrypted_pixels = data[bfOffBits:footer_start]

    return encrypted_key, nonce, original_pixel_len, header, encrypted_pixels

# ─── 解密 BMP ──────────────────────────────────────────────

def decrypt_bmp(private_key, data, output_path):
    """解密 BMP：恢复原始像素数据，还原完整 BMP"""
    print("🖼️  检测到加密的 BMP 文件")

    encrypted_key, nonce, original_pixel_len, header, encrypted_pixels = parse_bmp_footer(data)

    print(f"   文件头: {len(header)} bytes")
    print(f"   加密的像素数据: {len(encrypted_pixels)} bytes")
    print(f"   原始像素数据长度: {original_pixel_len} bytes")
    print(f"   GCM Nonce: {len(nonce)} bytes")
    print(f"   加密的AES密钥: {len(encrypted_key)} bytes")

    # 1. RSA-OAEP 解密 → 恢复 AES 会话密钥
    try:
        aes_key = private_key.decrypt(
            encrypted_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
    except Exception:
        print("❌ RSA 解密失败！私钥不匹配或密文已损坏。")
        sys.exit(1)

    print(f"🔑 RSA 解封成功，恢复 AES-{len(aes_key)*8} 会话密钥")

    # 2. AES-GCM 解密像素数据
    try:
        aesgcm = AESGCM(aes_key)
        pixel_data = aesgcm.decrypt(nonce, encrypted_pixels, None)
    except Exception:
        print("❌ AES-GCM 解密失败！文件可能已被篡改或损坏。")
        print("   GCM 认证标签校验未通过 —— 拒绝解密。")
        sys.exit(1)

    print(f"🔓 AES-GCM 解密成功 (完整性验证通过 ✅)")
    print(f"   恢复像素数据: {len(pixel_data)} bytes")

    # 3. 验证像素数据长度
    if len(pixel_data) != original_pixel_len:
        print(f"⚠️  警告: 像素数据长度不匹配 (预期 {original_pixel_len}, 实际 {len(pixel_data)})")
        print(f"   将使用实际解密结果")

    # 4. 还原完整 BMP
    restored = header + pixel_data

    # 更新 bfSize
    restored = restored[:2] + struct.pack("<I", len(restored)) + restored[6:]

    with open(output_path, "wb") as f:
        f.write(restored)

    print(f"\n✅ BMP 解密完成: {output_path}")
    print(f"   文件大小: {len(restored)} bytes")
    print(f"   💡 可用图片查看器打开查看原始图片")

# ─── 解密普通 .enc ─────────────────────────────────────────

def decrypt_regular(private_key, data, input_path, output_path):
    """
    解密混合加密的 .enc 包。

    包格式:
        [key_len: 4 bytes, big-endian]
        [encrypted_key: key_len bytes]
        [nonce: 12 bytes]
        [ct_len: 4 bytes, big-endian]
        [ciphertext: ct_len bytes]
    """
    # 手动解析（不用 BytesIO 避免依赖）
    offset = 0
    key_len = struct.unpack_from(">I", data, offset)[0]; offset += 4
    encrypted_key = data[offset:offset+key_len]; offset += key_len
    nonce = data[offset:offset+12]; offset += 12
    ct_len = struct.unpack_from(">I", data, offset)[0]; offset += 4
    ciphertext = data[offset:offset+ct_len]

    print(f"📦 读取加密包: {input_path}")
    print(f"   加密的AES密钥: {len(encrypted_key)} bytes")
    print(f"   GCM Nonce:     {len(nonce)} bytes")
    print(f"   密文+认证标签:  {len(ciphertext)} bytes")

    # 1. RSA-OAEP 解密 → 恢复 AES 会话密钥
    try:
        aes_key = private_key.decrypt(
            encrypted_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
    except Exception:
        print("❌ RSA 解密失败！私钥不匹配或密文已损坏。")
        sys.exit(1)

    print(f"🔑 RSA 解封成功，恢复 AES-{len(aes_key)*8} 会话密钥")

    # 2. AES-GCM 解密
    try:
        aesgcm = AESGCM(aes_key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception:
        print("❌ AES-GCM 解密失败！文件可能已被篡改或损坏。")
        print("   GCM 认证标签校验未通过 —— 拒绝解密。")
        sys.exit(1)

    print(f"🔓 AES-GCM 解密成功 (完整性验证通过 ✅)")

    # 3. 输出
    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"\n✅ 解密完成: {output_path}")
    print(f"   加密包大小: {os.path.getsize(input_path)} bytes")
    print(f"   恢复大小:   {len(plaintext)} bytes")

# ─── 主解密入口 ────────────────────────────────────────────

def decrypt_file(input_path, privkey_path="private_key.pem", output_path=None):
    """
    解密文件。自动检测格式：加密 BMP（含 HYBR 尾标）或 .enc 包。

    参数:
        input_path:  加密文件路径
        privkey_path: RSA 私钥 PEM 文件路径
        output_path: 解密输出路径（默认自动推断）
    """
    # 1. 加载私钥
    print(f"📂 加载私钥: {privkey_path}")
    private_key = load_private_key(privkey_path)

    # 2. 读取加密文件
    with open(input_path, "rb") as f:
        data = f.read()

    # 3. 检测格式
    if is_encrypted_bmp(data):
        if output_path is None:
            # 去掉 _encrypted 后缀，恢复原始文件名
            base, ext = os.path.splitext(input_path)
            if base.endswith("_encrypted"):
                output_path = base[:-10] + ext  # 去掉 _encrypted
            else:
                output_path = base + "_decrypted" + ext
        decrypt_bmp(private_key, data, output_path)
    else:
        if output_path is None:
            if input_path.endswith(".enc"):
                output_path = input_path[:-4]
            else:
                output_path = input_path + ".dec"
        decrypt_regular(private_key, data, input_path, output_path)

    return output_path

# ─── CLI ───────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    privkey = "private_key.pem"
    output = None

    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--key" and i + 1 < len(args):
            privkey = args[i + 1]
            i += 2
        elif args[i] == "--out" and i + 1 < len(args):
            output = args[i + 1]
            i += 2
        else:
            i += 1

    decrypt_file(input_file, privkey, output)
