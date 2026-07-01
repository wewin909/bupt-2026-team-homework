"""
实验2：混合加密实验 —— RSA密钥封装 + AES数据加密

场景模拟：
  Alice 与 Bob 之间需要安全传输一条消息。

流程：
  1. Alice 生成 RSA-2048 公私钥对，将公钥发送给 Bob
  2. Bob:
     a) 随机生成一个 AES-256 会话密钥（Session Key）
     b) 用 AES-256-GCM 加密明文（数据封装 —— 高效）
     c) 用 Alice 的 RSA 公钥加密该 AES 会话密钥（密钥封装 —— 安全）
     d) 将 {加密的会话密钥, IV, 密文, Tag} 发送给 Alice
  3. Alice:
     a) 用 RSA 私钥解密出 AES 会话密钥
     b) 用 AES 会话密钥解密出明文

设计说明：
  - 密钥封装: RSA-2048 + OAEP(SHA-256)
    解决对称密钥的安全分发问题
  - 数据封装: AES-256-GCM（Galois/Counter Mode）
    GCM 模式同时提供机密性和完整性认证（AEAD），
    防篡改且性能优于 CBC+HMAC 组合
  - 会话密钥: 一次性随机生成，用完即弃（前向安全性考量）

参考资料：
  - RFC 8017: PKCS #1 v2.2 (RSA-OAEP)
  - NIST SP 800-38D: GCM mode
  - TLS 1.3 中广泛采用类似的混合加密模式
"""

import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# ─── 工具函数 ─────────────────────────────────────────────

def bytes_to_hex(data: bytes) -> str:
    return data.hex()


def print_separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ═══════════════════════════════════════════════════════════
# 阶段一: Alice 生成密钥对
# ═══════════════════════════════════════════════════════════

class Alice:
    """
    Alice —— 消息接收方

    职责:
      1. 生成 RSA 公私钥对
      2. 发布公钥（或证书）
      3. 用自己的私钥解密收到的消息
    """

    def __init__(self, key_size: int = 2048):
        print(f"\n👩 Alice: 正在生成 RSA-{key_size} 密钥对...")
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )
        self.public_key = self._private_key.public_key()
        print(f"   ✅ 密钥对生成完成")
        # 打印公钥指纹
        pub_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        digest = hashes.Hash(hashes.SHA256())
        digest.update(pub_bytes)
        fingerprint = digest.finalize()
        print(f"   📜 公钥指纹 (SHA-256): {bytes_to_hex(fingerprint)[:16]}...")

    def decrypt_hybrid_message(self, encrypted_key: bytes,
                                nonce: bytes, ciphertext: bytes) -> str:
        """
        解密 Bob 发来的混合加密消息。

        参数:
            encrypted_key: RSA 加密的 AES 会话密钥
            nonce: AES-GCM 使用的 nonce
            ciphertext: AES-GCM 加密的密文（含认证标签）

        返回:
            明文字符串
        """
        # 1. RSA 解密 → 获取 AES 会话密钥
        aes_key = self._private_key.decrypt(
            encrypted_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        print(f"   🔑 成功解密出 AES 会话密钥（{len(aes_key)*8} bits）")

        # 2. AES-GCM 解密 → 获取明文
        aesgcm = AESGCM(aes_key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, None).decode("utf-8")
        print(f"   🔓 成功解密出明文")

        return plaintext


# ═══════════════════════════════════════════════════════════
# 阶段二: Bob 加密消息
# ═══════════════════════════════════════════════════════════

class Bob:
    """
    Bob —— 消息发送方

    职责:
      1. 生成一次性 AES-256 会话密钥
      2. 用 AES-256-GCM 加密明文（数据封装）
      3. 用 Alice 的 RSA 公钥加密会话密钥（密钥封装）
      4. 发送 {加密密钥, nonce, 密文} 给 Alice
    """

    def encrypt_hybrid_message(self, plaintext: str,
                                alice_public_key) -> dict:
        """
        执行混合加密。

        参数:
            plaintext: 要发送的明文
            alice_public_key: Alice 的 RSA 公钥

        返回:
            dict: {encrypted_key, nonce, ciphertext}
        """
        # 1. 生成一次性 AES-256 会话密钥
        aes_key = AESGCM.generate_key(bit_length=256)  # 256 bits
        print(f"   🎲 生成一次性 AES-256 会话密钥")
        print(f"      密钥 (hex): {bytes_to_hex(aes_key)}")

        # 2. AES-GCM 加密明文（数据封装）
        aesgcm = AESGCM(aes_key)
        nonce = os.urandom(12)  # GCM 推荐 96-bit nonce
        # 将明文编码为 bytes 再加密
        plaintext_bytes = plaintext.encode("utf-8")
        # AESGCM.encrypt 返回 ciphertext + 16-byte 认证标签（自动拼接）
        ciphertext = aesgcm.encrypt(nonce, plaintext_bytes, None)
        print(f"   🔒 AES-GCM 加密完成")
        print(f"      nonce: {bytes_to_hex(nonce)}")
        print(f"      密文长度: {len(ciphertext)} bytes（含16-byte认证标签）")
        print(f"      明文长度: {len(plaintext_bytes)} bytes")

        # 3. RSA-OAEP 加密 AES 密钥（密钥封装）
        encrypted_key = alice_public_key.encrypt(
            aes_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        print(f"   🔐 RSA 密钥封装完成")
        print(f"      加密后的会话密钥长度: {len(encrypted_key)} bytes")

        return {
            "encrypted_key": encrypted_key,
            "nonce": nonce,
            "ciphertext": ciphertext,
        }


# ═══════════════════════════════════════════════════════════
# 演示主流程
# ═══════════════════════════════════════════════════════════

def demo_hybrid() -> None:
    """演示混合加密的完整流程"""
    print_separator("混合加密实验：RSA (密钥封装) + AES-256-GCM (数据封装)")

    # ── 1. Alice 生成密钥对 ──
    print(f"\n{'─'*60}")
    print(f"  阶段 1: Alice 生成 RSA 密钥对")
    print(f"{'─'*60}")
    alice = Alice(key_size=2048)

    # ── 2. Bob 加密消息 ──
    print(f"\n{'─'*60}")
    print(f"  阶段 2: Bob 使用混合加密发送消息")
    print(f"{'─'*60}")
    bob = Bob()

    original_message = (
        "我已力竭，我已沉默，我已投降，我已绝望，我已崩溃，我已无助，我已流泪，我已求佛，我已倒下，我已上吊，我已卧轨，我已归隐田园，我已贤者时刻，我已无力招架，我已求天求地求爹娘，我已三十六计走为上计，我已装疯卖傻一问三不知。"
    )
    print(f"\n   📝 原始消息:\n      '{original_message}'")

    encrypted_package = bob.encrypt_hybrid_message(
        original_message, alice.public_key
    )

    # ── 3. 模拟网络传输 ──
    print(f"\n{'─'*60}")
    print(f"  阶段 3: 网络传输")
    print(f"{'─'*60}")
    print(f"   📡 传输数据包:")
    print(f"      - RSA加密的会话密钥: {len(encrypted_package['encrypted_key'])} bytes")
    print(f"      - GCM Nonce:          {len(encrypted_package['nonce'])} bytes")
    print(f"      - AES密文(+Tag):      {len(encrypted_package['ciphertext'])} bytes")
    print(f"      - 总传输量:            {sum(len(v) for v in encrypted_package.values())} bytes")

    # ── 4. Alice 解密消息 ──
    print(f"\n{'─'*60}")
    print(f"  阶段 4: Alice 解密消息")
    print(f"{'─'*60}")

    decrypted = alice.decrypt_hybrid_message(
        encrypted_package["encrypted_key"],
        encrypted_package["nonce"],
        encrypted_package["ciphertext"],
    )

    print(f"\n   📝 解密结果:\n      '{decrypted}'")

    # ── 验证 ──
    print(f"\n{'─'*60}")
    print(f"  验证")
    print(f"{'─'*60}")
    assert decrypted == original_message, "解密结果与原文不匹配！"
    print(f"   ✅ 验证通过：混合加密/解密结果与原文完全一致！")

    # ── 算法与参数总结 ──
    print(f"\n{'─'*60}")
    print(f"  算法与参数总结")
    print(f"{'─'*60}")
    print(f"""
    ┌─────────────────┬──────────────────────────────┐
    │ 组件            │ 算法 / 参数                  │
    ├─────────────────┼──────────────────────────────┤
    │ 密钥封装 (KEM)  │ RSA-2048 + OAEP(SHA-256)     │
    │ 数据封装 (DEM)  │ AES-256-GCM (AEAD)           │
    │ RSA 密钥长度     │ 2048 bits                    │
    │ AES 密钥长度     │ 256 bits                     │
    │ 公钥指数 e       │ 65537                        │
    │ GCM Nonce        │ 96 bits (随机生成)            │
    │ 认证标签         │ 128 bits (GCM 自动附加)       │
    └─────────────────┴──────────────────────────────┘
    """)


if __name__ == "__main__":
    demo_hybrid()
