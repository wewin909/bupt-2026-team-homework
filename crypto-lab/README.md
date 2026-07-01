# 密码学实验：对称加密、非对称加密与混合加密

本项目使用 Python 和 `cryptography` 库实现了三个密码学实验，涵盖对称加密、非对称加密和混合加密的核心原理。

## 项目结构

```
crypto-lab/
├── README.md           # 本文件
├── requirements.txt    # Python 依赖
├── aes_demo.py         # 实验1-1: AES 对称加密
├── rsa_demo.py         # 实验1-2: RSA 非对称加密
└── hybrid_demo.py      # 实验2:   混合加密 (RSA + AES)
```

## 环境准备

```bash
# 创建虚拟环境（推荐）
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate      # macOS / Linux
# 或
venv\Scripts\activate         # Windows

# 安装依赖
pip install -r requirements.txt
```

## 实验一：基础加密算法

### 1-1 AES 对称加密

**文件**: [aes_demo.py](aes_demo.py)

```bash
python aes_demo.py
```

| 参数 | 值 |
|------|-----|
| 算法 | AES（Advanced Encryption Standard） |
| 密钥长度 | 256 bits |
| 分组模式 | CBC（Cipher Block Chaining） |
| 填充方案 | PKCS7 |
| IV 长度 | 128 bits（随机生成） |

**核心流程**：
1. 生成 256-bit 随机密钥
2. 生成随机 IV，使用 AES-CBC 加密明文
3. 使用相同密钥和 IV 解密密文
4. 验证解密结果与原文一致

**关键代码说明**：
- `aes_encrypt()`: 接收明文和密钥，返回 `(iv, ciphertext)`
- `aes_decrypt()`: 接收密文、密钥和 IV，返回明文
- 使用 PKCS7 填充解决明文不是 16 字节整数倍的问题
- IV 随机生成，使相同明文每次加密产生不同密文

### 1-2 RSA 非对称加密

**文件**: [rsa_demo.py](rsa_demo.py)

```bash
python rsa_demo.py
```

| 参数 | 值 |
|------|-----|
| 算法 | RSA（Rivest–Shamir–Adleman） |
| 密钥长度 | 2048 bits |
| 公钥指数 e | 65537 |
| 填充方案 | OAEP（SHA-256 + MGF1） |

**核心流程**：
1. 生成 RSA-2048 公私钥对
2. 使用公钥加密明文
3. 使用私钥解密密文
4. 验证解密结果与原文一致

**关键代码说明**：
- `generate_rsa_keypair()`: 生成 2048-bit RSA 密钥对
- `rsa_encrypt()`: 使用公钥和 OAEP 填充加密
- `rsa_decrypt()`: 使用私钥和 OAEP 填充解密
- **注意**：RSA-2048 + OAEP(SHA-256) 单次最多加密约 190 bytes，因此实际中 RSA 只用于加密对称密钥

---

## 实验二：混合加密实验

**文件**: [hybrid_demo.py](hybrid_demo.py)

```bash
python hybrid_demo.py
```

### 设计思想

混合加密结合了两种加密范式的优势：

| | 对称加密 (AES) | 非对称加密 (RSA) |
|---|---|---|
| **速度** | 快 | 慢 |
| **密钥分发** | 困难（需安全信道） | 简单（公钥可公开） |
| **数据量** | 无限制 | 受密钥长度限制 |
| **用途** | 大批量数据加密 | 小量数据 / 密钥加密 |

**混合加密 = RSA 密钥封装 + AES 数据加密**

### 实验场景

Alice 和 Bob 之间需要安全传输消息：

```
┌──────────────────────┐          ┌──────────────────────┐
│        Alice          │          │         Bob          │
│    （消息接收方）      │          │    （消息发送方）      │
├──────────────────────┤          ├──────────────────────┤
│ 1. 生成 RSA 密钥对    │          │                      │
│    - 公钥 (发布)      │──公钥──▶│ 2. 获取 Alice 的公钥  │
│    - 私钥 (保密)      │          │                      │
│                      │          │ 3. 生成 AES 会话密钥  │
│                      │          │ 4. AES 加密明文       │
│                      │          │ 5. RSA 加密会话密钥   │
│                      │          │                      │
│                      │◀─密文──│ 6. 发送加密数据包      │
│                      │          │   {E_RSA(K),         │
│                      │          │    nonce,             │
│ 7. RSA 解密获取      │          │    E_AES(m, K)}      │
│    AES 会话密钥       │          │                      │
│ 8. AES 解密获取明文   │          │                      │
└──────────────────────┘          └──────────────────────┘
```

### 算法与参数

| 组件 | 算法 / 参数 | 说明 |
|------|-------------|------|
| **密钥封装 (KEM)** | RSA-2048 + OAEP(SHA-256) | 用接收方公钥加密对称密钥 |
| **数据封装 (DEM)** | AES-256-GCM | 用对称密钥加密实际数据 |
| RSA 密钥长度 | 2048 bits | 当前广泛采用的安全级别 |
| AES 密钥长度 | 256 bits | 最高安全级别 |
| GCM Nonce | 96 bits（随机生成） | 防重放攻击 |
| GCM 认证标签 | 128 bits | 提供完整性和真实性认证 |

### 为什么选择 GCM 模式？

AES-GCM 是一种 **AEAD**（Authenticated Encryption with Associated Data）模式：

- ✅ **机密性**：加密数据，无法被窃听
- ✅ **完整性**：检测数据是否被篡改
- ✅ **认证性**：确认密文来自持有正确密钥的发送方
- ✅ **高性能**：支持硬件加速（AES-NI / ARM Crypto Extensions）

相比 AES-CBC + 独立 HMAC 的构造，GCM 将加密和认证合为一体，代码更简洁且更不易出错。

### 为什么选择 OAEP 填充？

教科书式 RSA（直接对明文做模幂运算）存在多种攻击，包括：
- 选择密文攻击（CCA）
- 小指数攻击（当 e 较小时）
- 共模攻击

OAEP（Optimal Asymmetric Encryption Padding）通过引入随机填充和哈希函数，使 RSA 达到 **IND-CCA2** 安全（适应性选择密文攻击下的不可区分性）。

---

## 安全性说明

⚠️ **重要**：本项目仅用于教学演示。生产环境中应使用 TLS 等经过充分审计的协议，而非自行实现加密方案。

| 安全考量 | 本实验的做法 |
|----------|-------------|
| 密钥长度 | AES-256，RSA-2048（均符合 NIST 建议） |
| 填充方案 | OAEP（RSA）+ GCM 内置认证（AES） |
| 随机数 | 使用 `os.urandom()`（密码学安全随机源） |
| 会话密钥 | 一次性随机生成，用完即弃 |
| 前向安全性 | ⚠️ 本实验未实现（需 ECDHE 等 DH 密钥交换） |
| 密钥管理 | ⚠️ 本实验未涉及（需 PKI / 证书体系） |

---

## 参考资料

- [RFC 8017 - PKCS #1 v2.2: RSA Cryptography Specifications](https://datatracker.ietf.org/doc/html/rfc8017)
- [NIST SP 800-38D - GCM Mode](https://csrc.nist.gov/publications/detail/sp/800-38d/final)
- [NIST SP 800-57 - Key Management Recommendations](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev/5/final)
- [Cryptography.io 官方文档](https://cryptography.io/)

---

## 运行所有实验

```bash
echo "=== 实验1-1: AES 对称加密 ==="
python aes_demo.py

echo ""
echo "=== 实验1-2: RSA 非对称加密 ==="
python rsa_demo.py

echo ""
echo "=== 实验2: 混合加密 ==="
python hybrid_demo.py
```
