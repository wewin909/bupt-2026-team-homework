import os
import sys
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

AES_KEY_SIZE = 256   # bits
AES_BLOCK = 16        # bytes

# ─── BMP 读写 ───────────────────────────────────────────────

def read_bmp(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:2] != b"BM":
        raise ValueError("不是 BMP 文件")
    bfOffBits = struct.unpack_from("<I", data, 10)[0]
    return data[:bfOffBits], data[bfOffBits:], data

def write_bmp(header, pixel_area, out_path):
    """写入 BMP，pixel_area 包含显示像素 + 可能的尾部元数据"""
    output = bytearray(header + pixel_area)
    struct.pack_into("<I", output, 2, len(output))
    with open(out_path, "wb") as f:
        f.write(output)
    return len(output)

# ─── 各模式加密 ────────────────────────────────────────────

def encrypt_ecb(key, header, pixels, out_path):
    """
    ECB — Electronic Codebook（电子密码本）

    原理: Pᵢ → E_K(Pᵢ)，每个明文块独立加密
    特点: 相同明文块 → 相同密文块
    致命缺陷: 暴露数据模式/结构，图像轮廓清晰可见
    """
    # 像素数据恰好是 16 的倍数，无需填充
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    enc = cipher.encryptor()
    ct = enc.update(pixels) + enc.finalize()

    # 全部密文进入像素区（恰好等于原长度）
    write_bmp(header, ct, out_path)


def encrypt_cbc(key, header, pixels, out_path):
    """
    CBC — Cipher Block Chaining（密码分组链接）

    原理: Cᵢ = E_K(Pᵢ ⊕ Cᵢ₋₁)，需要随机 IV 作为 C₀
    特点: 相同明文块 → 不同密文块（IV 引入随机性）
    缺陷: 无完整性保护，可被比特翻转攻击（翻转 Cᵢ 的 bit b
          会在解密后翻转 Pᵢ₊₁ 的 bit b）
    """
    iv = os.urandom(AES_BLOCK)

    # PKCS7 填充（原文是整块也要加一个完整块）
    padder = padding.PKCS7(128).padder()
    padded = padder.update(pixels) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    enc = cipher.encryptor()
    ct = enc.update(padded) + enc.finalize()

    # 像素区 = 密文(截断到原长度) + IV 藏在末尾
    # BMP 阅读器根据 width*height*bpp 读像素，尾部多余字节会被忽略
    pixel_area = ct[:len(pixels)] + iv
    write_bmp(header, pixel_area, out_path)


def encrypt_ctr(key, header, pixels, out_path):
    """
    CTR — Counter（计数器模式，流密码）

    原理: Cᵢ = Pᵢ ⊕ E_K(nonce || counter)
    特点: 不需要填充，可并行，密文长度 = 明文长度
    缺陷: 无完整性保护，比特翻转攻击直接翻转对应明文比特
          （比 CBC 更危险——不需要相邻块传播）
    """
    nonce = os.urandom(AES_BLOCK)

    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    enc = cipher.encryptor()
    ct = enc.update(pixels) + enc.finalize()  # 长度 = 明文长度

    # nonce 藏在像素区末尾
    pixel_area = ct + nonce
    write_bmp(header, pixel_area, out_path)


def encrypt_gcm_demo(key, header, pixels, out_path):
    """
    GCM — Galois/Counter Mode（AEAD）

    原理: CTR 加密 + GHASH 多项式认证 → AEAD
    特点: 机密性 + 完整性 + 认证，三位一体
    优势: 任何密文篡改 → 认证标签验证失败 → 拒绝解密
          （CBC/CTR 被篡改后静默解密出错误数据，GCM 直接报警）
    """
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    # encrypt() 返回 ciphertext || 16-byte auth tag
    output = aesgcm.encrypt(nonce, pixels, None)
    ct = output[:-16]
    tag = output[-16:]

    # 像素区 = 密文 + nonce + tag 藏在末尾
    pixel_area = ct + nonce + tag
    write_bmp(header, pixel_area, out_path)


# ─── 主流程 ────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    bmp_path = sys.argv[1]
    base = os.path.splitext(bmp_path)[0]

    print(f"🔑 生成 AES-{AES_KEY_SIZE} 密钥（所有模式共用）")
    key = AESGCM.generate_key(bit_length=AES_KEY_SIZE)

    print(f"📂 读取 BMP: {bmp_path}")
    header, pixels, _ = read_bmp(bmp_path)
    print(f"   文件头: {len(header)} bytes, 像素数据: {len(pixels)} bytes")
    print(f"   图像尺寸: {struct.unpack_from('<i', header, 18)[0]}×{struct.unpack_from('<i', header, 22)[0]}")
    print()

    modes_list = [
        ("ECB", encrypt_ecb, "_ecb.bmp",
         "⚠️ 应能看到原始图像轮廓——这恰恰是 ECB 不安全的原因"),
        ("CBC", encrypt_cbc, "_cbc.bmp",
         "🔒 完全随机噪点——但缺乏完整性保护（可被比特翻转攻击）"),
        ("CTR", encrypt_ctr, "_ctr.bmp",
         "🔒 完全随机噪点——同样缺乏完整性保护"),
        ("GCM", encrypt_gcm_demo, "_gcm.bmp",
         "✅ 完全随机噪点 + 防篡改认证——现代加密标准"),
    ]

    for name, func, suffix, note in modes_list:
        out = base + suffix
        func(key, header, pixels, out)
        print(f"  [{name}] {out} — {note}")


if __name__ == "__main__":
    main()
