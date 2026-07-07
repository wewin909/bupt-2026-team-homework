import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


# ─── 工具函数 ─────────────────────────────────────────────

def bytes_to_hex(data: bytes) -> str:
    """将字节数据转为可读的十六进制字符串"""
    return data.hex()


def print_separator(title: str) -> None:
    """打印带标题的分隔线"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ─── AES 加密 / 解密 ──────────────────────────────────────

def aes_encrypt(plaintext: str, key: bytes) -> tuple[bytes, bytes]:
    """
    使用 AES-256-CBC 加密明文。

    参数:
        plaintext: 明文字符串
        key: 256-bit 密钥 (32 bytes)

    返回:
        (iv, ciphertext): 初始化向量和密文
    """
    # 1. 生成随机的 128-bit IV（初始化向量）
    iv = os.urandom(16)

    # 2. 创建 AES-CBC Cipher 对象（加密方向）
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
    )
    encryptor = cipher.encryptor()

    # 3. PKCS7 填充 —— AES 要求明文长度为 16 bytes 的整数倍
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode("utf-8")) + padder.finalize()

    # 4. 执行加密
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv, ciphertext


def aes_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> str:
    """
    使用 AES-256-CBC 解密密文。

    参数:
        ciphertext: 密文字节
        key: 256-bit 密钥 (32 bytes)
        iv: 加密时使用的初始化向量

    返回:
        明文字符串
    """
    # 1. 创建 AES-CBC Cipher 对象（解密方向）
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
    )
    decryptor = cipher.decryptor()

    # 2. 执行解密
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # 3. 去除 PKCS7 填充
    unpadder = padding.PKCS7(128).unpadder()
    plaintext_bytes = unpadder.update(padded_data) + unpadder.finalize()

    return plaintext_bytes.decode("utf-8")


# ─── 演示 ─────────────────────────────────────────────────

def demo_aes() -> None:
    """演示 AES 加密解密的完整流程"""
    print_separator("AES-256-CBC 对称加密实验")

    # 明文
    plaintext = "我已力竭，我已沉默，我已投降，我已绝望，我已崩溃，我已无助，我已流泪，我已求佛，我已倒下，我已上吊，我已卧轨，我已归隐田园，我已贤者时刻，我已无力招架，我已求天求地求爹娘，我已三十六计走为上计，我已装疯卖傻一问三不知。"
    print(f"\n📝 明文: {plaintext}")

    # 生成 256-bit 随机密钥
    key = os.urandom(32)  # 32 bytes = 256 bits
    print(f"🔑 密钥 (256-bit): {bytes_to_hex(key)}")

    # 加密
    iv, ciphertext = aes_encrypt(plaintext, key)
    print(f"🎲 初始化向量 IV (128-bit): {bytes_to_hex(iv)}")
    print(f"🔒 密文: {bytes_to_hex(ciphertext)}")
    print(f"📏 密文长度: {len(ciphertext)} bytes")

    # 解密
    decrypted = aes_decrypt(ciphertext, key, iv)
    print(f"🔓 解密结果: {decrypted}")

    # 验证
    assert decrypted == plaintext, "解密结果与原文不匹配！"
    print(f"\n✅ 验证通过：解密结果与原文一致！")

    # ── 错误密钥演示 ──
    print(f"\n--- 错误密钥解密演示 ---")
    wrong_key = os.urandom(32)
    try:
        aes_decrypt(ciphertext, wrong_key, iv)
    except Exception:
        print("❌ 使用错误密钥解密失败（填充校验错误），符合预期。")


if __name__ == "__main__":
    demo_aes()
