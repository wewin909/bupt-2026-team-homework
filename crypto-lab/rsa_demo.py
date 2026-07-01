"""
实验1-2：RSA非对称加密算法 —— 加密与解密

RSA 基于大整数分解的数学难题，使用一对密钥：
- 公钥 (n, e): 用于加密，可公开分享
- 私钥 (n, d): 用于解密，必须保密

本实验使用 2048-bit RSA 密钥（安全强度约 112 bits），
搭配 OAEP（Optimal Asymmetric Encryption Padding）填充方案，
避免教科书式 RSA 的已知安全问题。

关键参数说明：
  - 密钥长度: 2048 bits —— 当前广泛采用的安全级别
  - 公钥指数 e: 65537 —— 最常用的选择，兼顾安全与效率
  - 填充方案: OAEP with SHA-256 —— 防止选择密文攻击（CCA）
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization


# ─── 工具函数 ─────────────────────────────────────────────

def bytes_to_hex(data: bytes) -> str:
    return data.hex()


def print_separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ─── RSA 密钥生成 ─────────────────────────────────────────

def generate_rsa_keypair(key_size: int = 2048):
    """
    生成 RSA 公私钥对。

    参数:
        key_size: 密钥长度（bits），默认 2048

    返回:
        (private_key, public_key)
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def serialize_keys(private_key, public_key) -> None:
    """将密钥导出为 PEM 格式并打印"""
    # 私钥 PEM
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    # 公钥 PEM
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    print(f"\n📜 私钥 (PKCS#8 PEM, 前200字符):")
    print(private_pem.decode()[:200] + "...")
    print(f"\n📜 公钥 (SubjectPublicKeyInfo PEM, 前200字符):")
    print(public_pem.decode()[:200] + "...")

    return private_pem, public_pem


# ─── RSA 加密 / 解密 ──────────────────────────────────────

def rsa_encrypt(plaintext: str, public_key) -> bytes:
    """
    使用 RSA 公钥加密明文。

    参数:
        plaintext: 明文字符串
        public_key: RSA 公钥对象

    返回:
        密文字节

    注意: RSA-2048 + OAEP(SHA-256) 最多加密 190 bytes 数据，
    因此 RSA 通常只用于加密对称密钥，而非直接加密大量数据。
    """
    ciphertext = public_key.encrypt(
        plaintext.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return ciphertext


def rsa_decrypt(ciphertext: bytes, private_key) -> str:
    """
    使用 RSA 私钥解密密文。

    参数:
        ciphertext: 密文字节
        private_key: RSA 私钥对象

    返回:
        明文字符串
    """
    plaintext_bytes = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext_bytes.decode("utf-8")


# ─── 演示 ─────────────────────────────────────────────────

def demo_rsa() -> None:
    """演示 RSA 加密解密的完整流程"""
    print_separator("RSA-2048 非对称加密实验")

    # 1. 密钥生成
    print(f"\n🔨 正在生成 RSA-2048 密钥对...")
    private_key, public_key = generate_rsa_keypair(key_size=2048)
    print(f"✅ 密钥对生成完成（2048 bits）")

    # 查看密钥
    serialize_keys(private_key, public_key)

    # 打印公钥参数
    pub_numbers = public_key.public_numbers()
    print(f"\n🔢 公钥参数:")
    print(f"   n (模数) 长度: {pub_numbers.n.bit_length()} bits")
    print(f"   e (公钥指数): {pub_numbers.e}")

    # 2. 加密
    plaintext = "我已力竭，我已沉默，我已投降。"
    print(f"\n📝 明文: {plaintext}")
    print(f"📏 明文长度: {len(plaintext.encode('utf-8'))} bytes")

    ciphertext = rsa_encrypt(plaintext, public_key)
    print(f"🔒 密文长度: {len(ciphertext)} bytes (= {len(ciphertext)*8} bits)")
    print(f"🔒 密文 (hex): {bytes_to_hex(ciphertext)[:80]}...")

    # 3. 解密
    decrypted = rsa_decrypt(ciphertext, private_key)
    print(f"🔓 解密结果: {decrypted}")

    # 验证
    assert decrypted == plaintext, "解密结果与原文不匹配！"
    print(f"\n✅ 验证通过：解密结果与原文一致！")

    # ── RSA 加密容量说明 ──
    print(f"\n💡 提示: RSA-2048 + OAEP(SHA-256) 单次最多加密约 190 bytes，")
    print(f"   因此实际应用中 RSA 通常仅用于加密对称密钥（密钥封装），")
    print(f"   数据主体使用 AES 等对称算法加密 —— 见混合加密实验。")


if __name__ == "__main__":
    demo_rsa()
