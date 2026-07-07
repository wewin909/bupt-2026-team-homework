import os
import sys
import struct
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ─── 常量 ──────────────────────────────────────────────────
RSA_KEY_SIZE = 2048
AES_KEY_SIZE = 256       # bits
GCM_NONCE_SIZE = 12      # bytes (96 bits, GCM 最优)
BMP_FOOTER_MAGIC = b'HYBR'  # BMP 加密尾部标识

# ─── 密钥生成 ──────────────────────────────────────────────

def generate_keypair(priv_path="private_key.pem", pub_path="public_key.pem"):
    """生成 RSA 密钥对并保存为 PEM 文件"""
    print(f"🔨 生成 RSA-{RSA_KEY_SIZE} 密钥对...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=RSA_KEY_SIZE,
    )
    public_key = private_key.public_key()

    # 保存私钥
    with open(priv_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ))
    os.chmod(priv_path, 0o600)  # 仅所有者可读写

    # 保存公钥
    with open(pub_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ))

    print(f"✅ 密钥对已生成:")
    print(f"   私钥: {priv_path}  (务必保密！)")
    print(f"   公钥: {pub_path}  (可公开分享)")
    return priv_path, pub_path

# ─── 加载公钥 ──────────────────────────────────────────────

def load_public_key(path):
    """从 PEM 文件加载 RSA 公钥"""
    if not os.path.exists(path):
        print(f"❌ 找不到公钥文件: {path}")
        print(f"   请先运行: python hybrid_encrypt.py --gen-key")
        print(f"   或指定路径: python hybrid_encrypt.py <文件> --pubkey <公钥路径>")
        sys.exit(1)
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

# ─── BMP 检测与解析 ────────────────────────────────────────

def is_bmp(data):
    """检查文件是否为 BMP 格式"""
    return len(data) >= 2 and data[:2] == b'BM'

def parse_bmp_header(data):
    """
    解析 BMP 文件头，返回 (header_data, pixel_data, bfOffBits, pixel_size)。
    """
    if len(data) < 14:
        raise ValueError("文件太小，不是有效的 BMP")

    # BMP 文件头 (14 字节)
    bfType = data[0:2]
    bfSize = struct.unpack_from("<I", data, 2)[0]
    bfOffBits = struct.unpack_from("<I", data, 10)[0]

    if bfType != b'BM':
        raise ValueError("不是 BMP 文件（缺少 BM 标识）")

    # DIB 头 (从字节 14 开始)
    if len(data) < bfOffBits:
        raise ValueError("BMP 文件头损坏：bfOffBits 超出文件范围")

    # 像素数据大小（用 bfSize - bfOffBits 比解析 DIB 更可靠）
    header = data[:bfOffBits]
    pixel_data = data[bfOffBits:bfSize]  # bfSize 可能小于实际文件大小
    if len(pixel_data) == 0:
        # fallback: 使用实际文件剩余部分
        pixel_data = data[bfOffBits:]

    return header, pixel_data, bfOffBits

# ─── 加密 BMP ──────────────────────────────────────────────

def encrypt_bmp(public_key, data, output_path):
    header, pixel_data, bfOffBits = parse_bmp_header(data)

    print(f"🖼️  检测到 BMP 文件 (文件头 {bfOffBits} bytes, 像素数据 {len(pixel_data)} bytes)")
    print(f"   模式: 保留文件头 + 仅加密像素数据 → 输出可打开的乱码图片")

    # 1. 生成一次性 AES-256 会话密钥
    aes_key = AESGCM.generate_key(bit_length=AES_KEY_SIZE)
    print(f"🎲 生成一次性 AES-256 会话密钥")

    # 2. AES-256-GCM 加密像素数据
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(GCM_NONCE_SIZE)
    encrypted_pixels = aesgcm.encrypt(nonce, pixel_data, None)
    print(f"🔒 AES-GCM 加密完成 (nonce={len(nonce)}B, 密文={len(encrypted_pixels)}B, 含16B认证标签)")

    # 3. RSA-OAEP 加密 AES 会话密钥
    encrypted_key = public_key.encrypt(
        aes_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    print(f"🔐 RSA 密钥封装完成 (加密后密钥: {len(encrypted_key)} bytes)")

    # 4. 构建尾部元数据: [encrypted_key][nonce:12B][original_pixel_len:4B BE][key_len:4B BE][magic:4B]
    #    这样从文件末尾反向解析时，可以先读到 key_len，再用它来读取 encrypted_key
    footer = b''
    footer += encrypted_key
    footer += nonce
    footer += struct.pack(">I", len(pixel_data))
    footer += struct.pack(">I", len(encrypted_key))
    footer += BMP_FOOTER_MAGIC

    # 5. 组装: header + encrypted_pixels + footer
    output = header + encrypted_pixels + footer

    # 6. 更新 BMP 文件头中的 bfSize（偏移 2，4 字节小端）
    output = output[:2] + struct.pack("<I", len(output)) + output[6:]

    with open(output_path, "wb") as f:
        f.write(output)

    overhead = len(encrypted_key) + len(nonce) + 12 + len(BMP_FOOTER_MAGIC)
    print(f"\n✅ BMP 加密完成: {output_path}")
    print(f"   原始像素数据: {len(pixel_data)} bytes")
    print(f"   加密后像素:   {len(encrypted_pixels)} bytes (+{len(encrypted_pixels) - len(pixel_data)}B GCM 开销)")
    print(f"   元数据尾部:   {overhead} bytes")
    print(f"   文件总大小:   {len(output)} bytes")
    print(f"   💡 可直接用图片查看器打开查看噪点效果")

# ─── 加密普通文件 ──────────────────────────────────────────

def encrypt_regular(public_key, data, input_path, output_path):
    """普通文件加密：整个文件打包为 .enc 加密包"""
    print(f"📄 普通文件模式 ({len(data)} bytes)")

    # 1. 生成一次性 AES-256 会话密钥
    aes_key = AESGCM.generate_key(bit_length=AES_KEY_SIZE)
    print(f"🎲 生成一次性 AES-256 会话密钥")

    # 2. AES-256-GCM 加密
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(GCM_NONCE_SIZE)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    print(f"🔒 AES-GCM 加密完成 (nonce={len(nonce)}B, 密文={len(ciphertext)}B, 含16B认证标签)")

    # 3. RSA-OAEP 加密 AES 会话密钥
    encrypted_key = public_key.encrypt(
        aes_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    print(f"🔐 RSA 密钥封装完成 (加密后密钥: {len(encrypted_key)} bytes)")

    # 4. 打包输出
    with open(output_path, "wb") as f:
        f.write(struct.pack(">I", len(encrypted_key)))
        f.write(encrypted_key)
        f.write(nonce)
        f.write(struct.pack(">I", len(ciphertext)))
        f.write(ciphertext)

    overhead = len(encrypted_key) + len(nonce) + 8
    print(f"\n✅ 加密完成: {output_path}")
    print(f"   原始大小:   {len(data)} bytes")
    print(f"   加密包大小: {overhead + len(ciphertext)} bytes")
    print(f"   开销:       {overhead} bytes (RSA密钥封装 {len(encrypted_key)}B + nonce {len(nonce)}B + 元数据 8B)")
    print(f"   膨胀比:     {(overhead + len(ciphertext)) / max(len(data), 1):.2f}×")

# ─── 主加密入口 ────────────────────────────────────────────

def encrypt_file(input_path, pubkey_path="public_key.pem", output_path=None):
    # 1. 检查输入文件
    if not os.path.exists(input_path):
        print(f"❌ 找不到输入文件: {input_path}")
        sys.exit(1)

    # 2. 加载公钥
    print(f"📂 加载公钥: {pubkey_path}")
    public_key = load_public_key(pubkey_path)

    # 3. 读取原始文件
    with open(input_path, "rb") as f:
        data = f.read()

    # 4. 检测文件类型，选择加密模式
    if is_bmp(data):
        # BMP 模式：保留文件头
        if output_path is None:
            base, _ = os.path.splitext(input_path)
            output_path = base + "_encrypted.bmp"
        encrypt_bmp(public_key, data, output_path)
    else:
        # 普通模式
        if output_path is None:
            output_path = input_path + ".enc"
        encrypt_regular(public_key, data, input_path, output_path)

    return output_path

# ─── CLI ───────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "--gen-key":
        generate_keypair()
    else:
        input_file = sys.argv[1]
        pubkey = "public_key.pem"
        output = None

        # 解析可选参数
        args = sys.argv[2:]
        i = 0
        while i < len(args):
            if args[i] == "--pubkey" and i + 1 < len(args):
                pubkey = args[i + 1]
                i += 2
            elif args[i] == "--out" and i + 1 < len(args):
                output = args[i + 1]
                i += 2
            else:
                i += 1

        encrypt_file(input_file, pubkey, output)
