### TLS 1.2
## new Handshake
## Client Hello
Frame 2183: Packet, 276 bytes on wire (2208 bits), 276 bytes captured (2208 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd), Dst: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00)
Internet Protocol Version 4, Src: 10.21.138.45, Dst: 104.154.89.105
Transmission Control Protocol, Src Port: 64737, Dst Port: 1012, Seq: 1, Ack: 1, Len: 222
    Source Port: 64737
    Destination Port: 1012
    [Stream index: 41]
    [Stream Packet Number: 4]
    [Conversation completeness: Complete, WITH_DATA (63)]
    [TCP Segment Len: 222]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 491264507
    [Next Sequence Number: 223    (relative sequence number)]
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 1471708077
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
    Window: 255
    [Calculated window size: 65280]
    [Window size scaling factor: 256]
    Checksum: 0xff08 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
    [SEQ/ACK analysis]
    [Client Contiguous Streams: 1]
    [Server Contiguous Streams: 1]
    TCP payload (222 bytes)
Transport Layer Security
    [Stream index: 23]
    TLSv1.2 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 217
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 213
            Version: TLS 1.2 (0x0303)
            Random: d0c0005fa5dee6ebd152397e20bf3f798c040bdb9e91db58f615d405da370f9a
            Session ID Length: 0
            Cipher Suites Length: 56
            Cipher Suites (28 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
            Extensions Length: 116
            Extension: server_name (len=24) name=tls-v1-2.badssl.com
                Type: server_name (0)
                Length: 24
                Server Name Indication extension
            Extension: ec_point_formats (len=4)
                Type: ec_point_formats (11)
                Length: 4
                EC point formats Length: 3
                Elliptic curves point formats (3)
            Extension: supported_groups (len=12)
                Type: supported_groups (10)
                Length: 12
                Supported Groups List Length: 10
                Supported Groups (5 groups)
            Extension: session_ticket (len=0)
                Type: session_ticket (35)
                Length: 0
                Session Ticket: <MISSING>
            Extension: encrypt_then_mac (len=0)
                Type: encrypt_then_mac (22)
                Length: 0
            Extension: extended_master_secret (len=0)
                Type: extended_master_secret (23)
                Length: 0
            Extension: signature_algorithms (len=48)
                Type: signature_algorithms (13)
                Length: 48
                Signature Hash Algorithms Length: 46
                Signature Hash Algorithms (23 algorithms)
            [JA4: t12d280700_d943125447b4_3c5a66c06c35]
            [JA4_r […]: t12d280700_002f,0033,0035,0039,003c,003d,0067,006b,009c,009d,009e,009f,00ff,c009,c00a,c013,c014,c023,c024,c027,c028,c02b,c02c,c02f,c030,cca8,cca9,ccaa_000a,000b,000d,0016,0017,0023_0403,0503,0603,0807,0808,0809,080a,080b,0804,]
            [JA3 Fullstring: 771,49196-49200-159-52393-52392-52394-49195-49199-158-49188-49192-107-49187-49191-103-49162-49172-57-49161-49171-51-157-156-61-60-53-47-255,0-11-10-35-22-23-13,29-23-30-25-24,0-1-2]
            [JA3: 871a754af286dfb70c1b53c6887c62e0]


## Server Hello
Frame 2184: Packet, 1436 bytes on wire (11488 bits), 1436 bytes captured (11488 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00), Dst: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd)
Internet Protocol Version 4, Src: 104.154.89.105, Dst: 10.21.138.45
Transmission Control Protocol, Src Port: 1012, Dst Port: 64737, Seq: 1, Ack: 223, Len: 1382
Transport Layer Security
    [Stream index: 23]
    TLSv1.2 Record Layer: Handshake Protocol: Server Hello
        Content Type: Handshake (22)
        Version: TLS 1.2 (0x0303)
        Length: 61
        Handshake Protocol: Server Hello
            Handshake Type: Server Hello (2)
            Length: 57
            Version: TLS 1.2 (0x0303)
            Random: 230c9de8a37bbcb43c6adf077f61ee5dc74af15ca77d32fea9836c7e9d5b15e0
            Session ID Length: 0
            Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
            Compression Method: null (0)
            Extensions Length: 17
            Extension: renegotiation_info (len=1)
                Type: renegotiation_info (65281)
                Length: 1
                Renegotiation Info extension
            Extension: ec_point_formats (len=4)
                Type: ec_point_formats (11)
                Length: 4
                EC point formats Length: 3
                Elliptic curves point formats (3)
            Extension: session_ticket (len=0)
                Type: session_ticket (35)
                Length: 0
                Session Ticket: <MISSING>
            [JA3S Fullstring: 771,49200,65281-11-35]
            [JA3S: e35df3e00ca4ef31d42b34bebaa2f86e]
    TLS segment data (1316 bytes)

## recover
## Client Hello
Frame 3536: Packet, 500 bytes on wire (4000 bits), 500 bytes captured (4000 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd), Dst: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00)
Internet Protocol Version 4, Src: 10.21.138.45, Dst: 104.154.89.105
Transmission Control Protocol, Src Port: 63349, Dst Port: 1012, Seq: 1, Ack: 1, Len: 446
Transport Layer Security
    [Stream index: 31]
    TLSv1.2 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 441
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 437
            Version: TLS 1.2 (0x0303)
            Random: 35db4765c349b2fc87ce091d97d4c9b78391473618fda532a5d7c255685e8c2a
            Session ID Length: 32
            Session ID: e1a252bd62408b2bf8cfcd34e959bbc0920aea7e1fde7818d3a68143a64d9358
            Cipher Suites Length: 56
            Cipher Suites (28 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
            Extensions Length: 308
            Extension: server_name (len=24) name=tls-v1-2.badssl.com
                Type: server_name (0)
                Length: 24
                Server Name Indication extension
            Extension: ec_point_formats (len=4)
                Type: ec_point_formats (11)
                Length: 4
                EC point formats Length: 3
                Elliptic curves point formats (3)
            Extension: supported_groups (len=12)
                Type: supported_groups (10)
                Length: 12
                Supported Groups List Length: 10
                Supported Groups (5 groups)
            Extension: session_ticket (len=192)
                Type: session_ticket (35)
                Length: 192
                Session Ticket […]: 654b5ca80b33f83dda2ef3a291236802ef91317b765f74cb3999d298f0645bbb2575ac13df358d849310495b694205ef275af755f333455e9a4bae53459decde239318d381c0b4c8bafca2dbf2cdaf28b9ca130a80ba9b122dfd8bb44622d28b2ff772bb80d14b4d02bdd2464
            Extension: encrypt_then_mac (len=0)
                Type: encrypt_then_mac (22)
                Length: 0
            Extension: extended_master_secret (len=0)
                Type: extended_master_secret (23)
                Length: 0
            Extension: signature_algorithms (len=48)
                Type: signature_algorithms (13)
                Length: 48
                Signature Hash Algorithms Length: 46
                Signature Hash Algorithms (23 algorithms)
            [JA4: t12d280700_d943125447b4_3c5a66c06c35]
            [JA4_r […]: t12d280700_002f,0033,0035,0039,003c,003d,0067,006b,009c,009d,009e,009f,00ff,c009,c00a,c013,c014,c023,c024,c027,c028,c02b,c02c,c02f,c030,cca8,cca9,ccaa_000a,000b,000d,0016,0017,0023_0403,0503,0603,0807,0808,0809,080a,080b,0804,]
            [JA3 Fullstring: 771,49196-49200-159-52393-52392-52394-49195-49199-158-49188-49192-107-49187-49191-103-49162-49172-57-49161-49171-51-157-156-61-60-53-47-255,0-11-10-35-22-23-13,29-23-30-25-24,0-1-2]
            [JA3: 871a754af286dfb70c1b53c6887c62e0]

## Server Hello
Frame 3538: Packet, 191 bytes on wire (1528 bits), 191 bytes captured (1528 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00), Dst: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd)
Internet Protocol Version 4, Src: 104.154.89.105, Dst: 10.21.138.45
Transmission Control Protocol, Src Port: 1012, Dst Port: 63349, Seq: 1, Ack: 447, Len: 137
Transport Layer Security
    [Stream index: 31]
    TLSv1.2 Record Layer: Handshake Protocol: Server Hello
        Content Type: Handshake (22)
        Version: TLS 1.2 (0x0303)
        Length: 81
        Handshake Protocol: Server Hello
            Handshake Type: Server Hello (2)
            Length: 77
            Version: TLS 1.2 (0x0303)
            Random: 5a3d87dba04ded23d02ad3acc4e96d3718c4e43cd576cb4621024e22cba24d0a
            Session ID Length: 32
            Session ID: e1a252bd62408b2bf8cfcd34e959bbc0920aea7e1fde7818d3a68143a64d9358
            Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
            Compression Method: null (0)
            Extensions Length: 5
            Extension: renegotiation_info (len=1)
                Type: renegotiation_info (65281)
                Length: 1
                Renegotiation Info extension
            [JA3S Fullstring: 771,49200,65281]
            [JA3S: 364ff14b04ef93c3b4cfa429d729c0d9]
    TLSv1.2 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec
        Content Type: Change Cipher Spec (20)
        Version: TLS 1.2 (0x0303)
        Length: 1
        Change Cipher Spec Message
    TLSv1.2 Record Layer: Handshake Protocol: Encrypted Handshake Message
        Content Type: Handshake (22)
        Version: TLS 1.2 (0x0303)
        Length: 40
        Handshake Protocol: Encrypted Handshake Message


在 TLS 1.2 会话恢复过程中，客户端发送 Client Hello 后，服务器返回 Server Hello，随后双方很快进入 Change Cipher Spec 与
加密握手消息阶段，整个过程中未再出现 Certificate、Server Key Exchange 和 Server Hello Done 等完整握手报文。说明客户端
成功复用了之前建立的会话状态，减少了握手开销，提高了连接效率。

完整握手
nslookup tls-v1-2.badssl.com 查询IP地址
openssl s_client -connect tls-v1-2.badssl.com:1012 -servername tls-v1-2.badssl.com -tls1_2 -msg
会话恢复
openssl s_client -connect tls-v1-2.badssl.com:1012 -servername tls-v1-2.badssl.com -tls1_2 -reconnect

### TLS 1.3
## new Handshake
## Client Hello
Frame 11: Packet, 296 bytes on wire (2368 bits), 296 bytes captured (2368 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd), Dst: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00)
Internet Protocol Version 4, Src: 10.21.138.45, Dst: 104.16.124.96
Transmission Control Protocol, Src Port: 65411, Dst Port: 443, Seq: 1, Ack: 1, Len: 242
    Source Port: 65411
    Destination Port: 443
    [Stream index: 2]
    [Stream Packet Number: 4]
    [Conversation completeness: Complete, WITH_DATA (63)]
    [TCP Segment Len: 242]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 54787358
    [Next Sequence Number: 243    (relative sequence number)]
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 3584931917
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
    Window: 255
    [Calculated window size: 65280]
    [Window size scaling factor: 256]
    Checksum: 0x71fc [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
    [SEQ/ACK analysis]
    [Client Contiguous Streams: 1]
    [Server Contiguous Streams: 1]
    TCP payload (242 bytes)
Transport Layer Security
    [Stream index: 0]
    TLSv1.3 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 237
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 233
            Version: TLS 1.2 (0x0303)
            Random: 2c0aa5ee7134fa631f46de97acc68f621b4345c5d1f95ee65dd6d01069510b63
            Session ID Length: 32
            Session ID: 3941d8cc037cd964dc7796ca52e1c5a900444c444931bbe3a014cfa4631eecc1
            Cipher Suites Length: 8
            Cipher Suites (4 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
            Extensions Length: 152
            Extension: server_name (len=23) name=www.cloudflare.com
                Type: server_name (0)
                Length: 23
                Server Name Indication extension
            Extension: ec_point_formats (len=4)
                Type: ec_point_formats (11)
                Length: 4
                EC point formats Length: 3
                Elliptic curves point formats (3)
            Extension: supported_groups (len=12)
                Type: supported_groups (10)
                Length: 12
                Supported Groups List Length: 10
                Supported Groups (5 groups)
            Extension: session_ticket (len=0)
                Type: session_ticket (35)
                Length: 0
                Session Ticket: <MISSING>
            Extension: encrypt_then_mac (len=0)
                Type: encrypt_then_mac (22)
                Length: 0
            Extension: extended_master_secret (len=0)
                Type: extended_master_secret (23)
                Length: 0
            Extension: signature_algorithms (len=30)
                Type: signature_algorithms (13)
                Length: 30
                Signature Hash Algorithms Length: 28
                Signature Hash Algorithms (14 algorithms)
            Extension: supported_versions (len=3) TLS 1.3
                Type: supported_versions (43)
                Length: 3
                Supported Versions length: 2
                Supported Version: TLS 1.3 (0x0304)
            Extension: psk_key_exchange_modes (len=2)
                Type: psk_key_exchange_modes (45)
                Length: 2
                PSK Key Exchange Modes Length: 1
                PSK Key Exchange Mode: PSK with (EC)DHE key establishment (psk_dhe_ke) (1)
            Extension: key_share (len=38) x25519
                Type: key_share (51)
                Length: 38
                Key Share extension
            [JA4: t13d041000_16476d049b0b_78f1d400d464]
            [JA4_r: t13d041000_00ff,1301,1302,1303_000a,000b,000d,0016,0017,0023,002b,002d,0033_0403,0503,0603,0807,0808,0809,080a,080b,0804,0805,0806,0401,0501,0601]
            [JA3 Fullstring: 771,4866-4867-4865-255,0-11-10-35-22-23-13-43-45-51,29-23-30-25-24,0-1-2]
            [JA3: a66e498c488aa0523759691248cdfb01]


## Server Hello
Frame 13: Packet, 1436 bytes on wire (11488 bits), 1436 bytes captured (11488 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00), Dst: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd)
Internet Protocol Version 4, Src: 104.16.124.96, Dst: 10.21.138.45
Transmission Control Protocol, Src Port: 443, Dst Port: 65411, Seq: 1, Ack: 243, Len: 1382
    Source Port: 443
    Destination Port: 65411
    [Stream index: 2]
    [Stream Packet Number: 6]
    [Conversation completeness: Complete, WITH_DATA (63)]
    [TCP Segment Len: 1382]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 3584931917
    [Next Sequence Number: 1383    (relative sequence number)]
    Acknowledgment Number: 243    (relative ack number)
    Acknowledgment number (raw): 54787600
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x010 (ACK)
    Window: 16
    [Calculated window size: 131072]
    [Window size scaling factor: 8192]
    Checksum: 0x583c [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
    [SEQ/ACK analysis]
    [Client Contiguous Streams: 1]
    [Server Contiguous Streams: 1]
    TCP payload (1382 bytes)
    [Reassembled PDU in frame: 15]
    TCP segment data (1249 bytes)
Transport Layer Security
    [Stream index: 0]
    TLSv1.3 Record Layer: Handshake Protocol: Server Hello
        Content Type: Handshake (22)
        Version: TLS 1.2 (0x0303)
        Length: 122
        Handshake Protocol: Server Hello
            Handshake Type: Server Hello (2)
            Length: 118
            Version: TLS 1.2 (0x0303)
            Random: cd6a3f1c20fac6166f34cfee7d9f4ee0407c938f520efecd398e461e493c134b
            Session ID Length: 32
            Session ID: 3941d8cc037cd964dc7796ca52e1c5a900444c444931bbe3a014cfa4631eecc1
            Cipher Suite: TLS_AES_256_GCM_SHA384 (0x1302)
            Compression Method: null (0)
            Extensions Length: 46
            Extension: key_share (len=36) x25519
                Type: key_share (51)
                Length: 36
                Key Share extension
            Extension: supported_versions (len=2) TLS 1.3
                Type: supported_versions (43)
                Length: 2
                Supported Version: TLS 1.3 (0x0304)
            [JA3S Fullstring: 771,4866,51-43]
            [JA3S: 907bf3ecef1c987c889946b737b43de8]
    TLSv1.3 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec
        Content Type: Change Cipher Spec (20)
        Version: TLS 1.2 (0x0303)
        Length: 1
        Change Cipher Spec Message
    TLS segment data (1249 bytes)

## recover
## Client Hello
Frame 154: Packet, 567 bytes on wire (4536 bits), 567 bytes captured (4536 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd), Dst: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00)
Internet Protocol Version 4, Src: 10.21.138.45, Dst: 104.16.124.96
Transmission Control Protocol, Src Port: 53609, Dst Port: 443, Seq: 1, Ack: 1, Len: 513
    Source Port: 53609
    Destination Port: 443
    [Stream index: 16]
    [Stream Packet Number: 4]
    [Conversation completeness: Complete, WITH_DATA (63)]
    [TCP Segment Len: 513]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 3639708999
    [Next Sequence Number: 514    (relative sequence number)]
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 2149223708
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
    Window: 255
    [Calculated window size: 65280]
    [Window size scaling factor: 256]
    Checksum: 0xb44a [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
    [SEQ/ACK analysis]
    [Client Contiguous Streams: 1]
    [Server Contiguous Streams: 1]
    TCP payload (513 bytes)
Transport Layer Security
    [Stream index: 9]
    TLSv1.3 Record Layer: Handshake Protocol: Client Hello
        Content Type: Handshake (22)
        Version: TLS 1.0 (0x0301)
        Length: 508
        Handshake Protocol: Client Hello
            Handshake Type: Client Hello (1)
            Length: 504
            Version: TLS 1.2 (0x0303)
            Random: 91575460dfb5e75e3111f596359ed8e9c24dc649d595ef1ac7576cafe011a2f5
            Session ID Length: 32
            Session ID: 8dcbdce975c00b1469699ffca5f9e5689e591d8f6601cd38ff6196b0a0e43943
            Cipher Suites Length: 8
            Cipher Suites (4 suites)
            Compression Methods Length: 1
            Compression Methods (1 method)
            Extensions Length: 423
            Extension: server_name (len=23) name=www.cloudflare.com
                Type: server_name (0)
                Length: 23
                Server Name Indication extension
            Extension: ec_point_formats (len=4)
                Type: ec_point_formats (11)
                Length: 4
                EC point formats Length: 3
                Elliptic curves point formats (3)
            Extension: supported_groups (len=12)
                Type: supported_groups (10)
                Length: 12
                Supported Groups List Length: 10
                Supported Groups (5 groups)
            Extension: session_ticket (len=0)
                Type: session_ticket (35)
                Length: 0
                Session Ticket: <MISSING>
            Extension: encrypt_then_mac (len=0)
                Type: encrypt_then_mac (22)
                Length: 0
            Extension: extended_master_secret (len=0)
                Type: extended_master_secret (23)
                Length: 0
            Extension: signature_algorithms (len=30)
                Type: signature_algorithms (13)
                Length: 30
                Signature Hash Algorithms Length: 28
                Signature Hash Algorithms (14 algorithms)
            Extension: supported_versions (len=3) TLS 1.3
                Type: supported_versions (43)
                Length: 3
                Supported Versions length: 2
                Supported Version: TLS 1.3 (0x0304)
            Extension: psk_key_exchange_modes (len=2)
                Type: psk_key_exchange_modes (45)
                Length: 2
                PSK Key Exchange Modes Length: 1
                PSK Key Exchange Mode: PSK with (EC)DHE key establishment (psk_dhe_ke) (1)
            Extension: key_share (len=38) x25519
                Type: key_share (51)
                Length: 38
                Key Share extension
            Extension: pre_shared_key (len=267)
                Type: pre_shared_key (41)
                Length: 267
                Pre-Shared Key extension
            [JA4: t13d041100_16476d049b0b_6775ac8fe30b]
            [JA4_r: t13d041100_00ff,1301,1302,1303_000a,000b,000d,0016,0017,0023,0029,002b,002d,0033_0403,0503,0603,0807,0808,0809,080a,080b,0804,0805,0806,0401,0501,0601]
            [JA3 Fullstring: 771,4866-4867-4865-255,0-11-10-35-22-23-13-43-45-51-41,29-23-30-25-24,0-1-2]
            [JA3: c517dfad7b7ebce7003d4e3b943bc6d7]

## Server Hello
Frame 156: Packet, 273 bytes on wire (2184 bits), 273 bytes captured (2184 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00), Dst: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd)
Internet Protocol Version 4, Src: 104.16.124.96, Dst: 10.21.138.45
Transmission Control Protocol, Src Port: 443, Dst Port: 53609, Seq: 1, Ack: 514, Len: 219
    Source Port: 443
    Destination Port: 53609
    [Stream index: 16]
    [Stream Packet Number: 6]
    [Conversation completeness: Complete, WITH_DATA (63)]
    [TCP Segment Len: 219]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 2149223708
    [Next Sequence Number: 220    (relative sequence number)]
    Acknowledgment Number: 514    (relative ack number)
    Acknowledgment number (raw): 3639709512
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
    Window: 16
    [Calculated window size: 131072]
    [Window size scaling factor: 8192]
    Checksum: 0x9ee0 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
    [SEQ/ACK analysis]
    [Client Contiguous Streams: 1]
    [Server Contiguous Streams: 1]
    TCP payload (219 bytes)
Transport Layer Security
    [Stream index: 9]
    TLSv1.3 Record Layer: Handshake Protocol: Server Hello
        Content Type: Handshake (22)
        Version: TLS 1.2 (0x0303)
        Length: 128
        Handshake Protocol: Server Hello
            Handshake Type: Server Hello (2)
            Length: 124
            Version: TLS 1.2 (0x0303)
            Random: a15eeea0397a88b6e9eab31591aebf36956279b635d0721dd648b90ef4e967e7
            Session ID Length: 32
            Session ID: 8dcbdce975c00b1469699ffca5f9e5689e591d8f6601cd38ff6196b0a0e43943
            Cipher Suite: TLS_AES_256_GCM_SHA384 (0x1302)
            Compression Method: null (0)
            Extensions Length: 52
            Extension: pre_shared_key (len=2)
                Type: pre_shared_key (41)
                Length: 2
                Pre-Shared Key extension
            Extension: key_share (len=36) x25519
                Type: key_share (51)
                Length: 36
                Key Share extension
            Extension: supported_versions (len=2) TLS 1.3
                Type: supported_versions (43)
                Length: 2
                Supported Version: TLS 1.3 (0x0304)
            [JA3S Fullstring: 771,4866,41-51-43]
            [JA3S: f590053ff246338aff7c203dbe7164d6]
    TLSv1.3 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec
        Content Type: Change Cipher Spec (20)
        Version: TLS 1.2 (0x0303)
        Length: 1
        Change Cipher Spec Message
    TLSv1.3 Record Layer: Application Data Protocol: Hypertext Transfer Protocol
        Opaque Type: Application Data (23)
        Version: TLS 1.2 (0x0303)
        Length: 75
        Encrypted Application Data: 08b0fe5d40772773ea23d250367a76133720f6029110cae2e3b82bd55ce24f36520a4b2fb6700ad350cc184083a56c1ce25f14b9dba788ddfd20f92b252f98c1655cb37dc2a4be11adffbb
        [Application Data Protocol: Hypertext Transfer Protocol]


第一次建立连接并保存会话：
openssl s_client -connect www.cloudflare.com:443 -servername www.cloudflare.com -tls1_3 -sess_out tls13_sess.pem
第二次加载会话并抓包：
openssl s_client -connect www.cloudflare.com:443 -servername www.cloudflare.com -tls1_3 -sess_in tls13_sess.pem -msg

### QUIC
## new connection 
Frame 235: Packet, 1242 bytes on wire (9936 bits), 1242 bytes captured (9936 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd), Dst: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00)
Internet Protocol Version 4, Src: 10.21.138.45, Dst: 104.18.26.14
User Datagram Protocol, Src Port: 61400, Dst Port: 443
    Source Port: 61400
    Destination Port: 443
    Length: 1208
    Checksum: 0xe973 [unverified]
    [Checksum Status: Unverified]
    [Stream index: 2]
    [Stream Packet Number: 1]
    [Timestamps]
    UDP payload (1200 bytes)
QUIC IETF
    QUIC Connection information
        [Connection Number: 0]
    [Packet Length: 534]
    1... .... = Header Form: Long Header (1)
    .1.. .... = Fixed Bit: True
    ..00 .... = Packet Type: Initial (0)
    [.... 00.. = Reserved: 0]
    [.... ..01 = Packet Number Length: 2 bytes (1)]
    Version: 1 (0x00000001)
    Destination Connection ID Length: 8
    Destination Connection ID: 8e3fd0e70f5e8964
    Source Connection ID Length: 8
    Source Connection ID: fb4a8d4516aafdd1
    Token Length: 0
    Length: 508
    [Packet Number: 0]
    Payload […]: 1804b0a3bc8fb23f5e6684567191fbc13543a90b5c82e1d8b07fd9cc1a7b242366a4b49355069de10f0ed9557ef4c4147f1731a063b1e09303f6124e9434f2dbc450c2e801de08344ec677df3b0f158e07bd69f8fee88b1127256290226841dd6396ab7a06968298cbb7c77436f907e6
    CRYPTO
        Frame Type: CRYPTO (0x0000000000000006)
        Offset: 0
        Length: 486
        Crypto Data
        TLSv1.3 Record Layer: Handshake Protocol: Client Hello
            Handshake Protocol: Client Hello
                Handshake Type: Client Hello (1)
                Length: 482
                Version: TLS 1.2 (0x0303)
                    [Expert Info (Chat/Deprecated): This legacy_version field MUST be ignored. The supported_versions extension is present and MUST be used instead.]
                Random: cce25f3a3851004ba1e61c5829e3e3af4575479724864b17eb8e189e6390671c
                Session ID Length: 0
                Cipher Suites Length: 6
                Cipher Suites (3 suites)
                Compression Methods Length: 1
                Compression Methods (1 method)
                Extensions Length: 435
                Extension: key_share (len=268) secp256r1, secp384r1, x25519, x448
                    Type: key_share (51)
                    Length: 268
                    Key Share extension
                Extension: supported_versions (len=3) TLS 1.3
                    Type: supported_versions (43)
                    Length: 3
                    Supported Versions length: 2
                    Supported Version: TLS 1.3 (0x0304)
                Extension: signature_algorithms (len=20)
                    Type: signature_algorithms (13)
                    Length: 20
                    Signature Hash Algorithms Length: 18
                    Signature Hash Algorithms (9 algorithms)
                Extension: supported_groups (len=10)
                    Type: supported_groups (10)
                    Length: 10
                    Supported Groups List Length: 8
                    Supported Groups (4 groups)
                Extension: psk_key_exchange_modes (len=2)
                    Type: psk_key_exchange_modes (45)
                    Length: 2
                    PSK Key Exchange Modes Length: 1
                    PSK Key Exchange Mode: PSK with (EC)DHE key establishment (psk_dhe_ke) (1)
                Extension: server_name (len=24) name=cloudflare-quic.com
                    Type: server_name (0)
                    Length: 24
                    Server Name Indication extension
                Extension: application_layer_protocol_negotiation (len=5)
                    Type: application_layer_protocol_negotiation (16)
                    Length: 5
                    ALPN Extension Length: 3
                    ALPN Protocol
                Extension: quic_transport_parameters (len=71)
                    Type: quic_transport_parameters (57)
                    Length: 71
                    Parameter: max_idle_timeout (len=4) 60000 ms
                    Parameter: initial_max_data (len=4) 1048576
                    Parameter: initial_max_stream_data_bidi_local (len=4) 1048576
                    Parameter: initial_max_stream_data_bidi_remote (len=4) 1048576
                    Parameter: initial_max_stream_data_uni (len=4) 1048576
                    Parameter: initial_max_streams_bidi (len=2) 128
                    Parameter: initial_max_streams_uni (len=2) 128
                    Parameter: ack_delay_exponent (len=1)
                    Parameter: max_ack_delay (len=1) 25
                    Parameter: active_connection_id_limit (len=1) 8
                    Parameter: initial_source_connection_id (len=8)
                    Parameter: version_information (len=12)
                [JA4: q13d0308h3_55b375c5d22e_a06176d7f541]
                [JA4_r: q13d0308h3_1301,1302,1303_000a,000d,002b,002d,0033,0039_0403,0804,0401,0503,0805,0501,0201,0807,0808]
                [JA3 Fullstring: 771,4866-4865-4867,51-43-13-10-45-0-16-57,23-24-29-30,]
                [JA3: 273162b4249b4a9e8e66cf971794f989]
QUIC IETF
    [Expert Info (Note/Protocol): (Random) padding data appended to the datagram]

## reconnect
Frame 513: Packet, 1242 bytes on wire (9936 bits), 1242 bytes captured (9936 bits) on interface \Device\NPF_{30AFF14E-338B-4503-8C4C-F6CB6A3C66D1}, id 0
Ethernet II, Src: LiteonTechno_67:2c:dd (c0:35:32:67:2c:dd), Dst: HewlettPacka_6c:24:00 (10:4f:58:6c:24:00)
Internet Protocol Version 4, Src: 10.21.138.45, Dst: 104.18.26.14
User Datagram Protocol, Src Port: 52796, Dst Port: 443
    Source Port: 52796
    Destination Port: 443
    Length: 1208
    Checksum: 0xe92c [unverified]
    [Checksum Status: Unverified]
    [Stream index: 6]
    [Stream Packet Number: 1]
    [Timestamps]
    UDP payload (1200 bytes)
QUIC IETF
    QUIC Connection information
        [Connection Number: 0]
    [Packet Length: 825]
    1... .... = Header Form: Long Header (1)
    .1.. .... = Fixed Bit: True
    ..00 .... = Packet Type: Initial (0)
    [.... 00.. = Reserved: 0]
    [.... ..01 = Packet Number Length: 2 bytes (1)]
    Version: 1 (0x00000001)
    Destination Connection ID Length: 8
    Destination Connection ID: b81dd0ef0191e05a
    Source Connection ID Length: 8
    Source Connection ID: 63b1aa53498eea19
    Token Length: 0
    Length: 799
    [Packet Number: 0]
    Payload […]: 490044534442b4ef36d2620ee0a2c7e84467a29524c9d7d53b8b9786756a4103eeb12bf855d2d3ffbb6dc0b83fe1b306d2496cede6c6e1c313a4b16f8dbddec63347a35557b3cb32aedfd20d6a93e52151f53de0a3a5b7fa2b66af7d7204941732ea57af7f84e09e7f54c56d1592e6fa
    CRYPTO
        Frame Type: CRYPTO (0x0000000000000006)
        Offset: 0
        Length: 777
        Crypto Data
        TLSv1.3 Record Layer: Handshake Protocol: Client Hello
            Handshake Protocol: Client Hello
                Handshake Type: Client Hello (1)
                Length: 773
                Version: TLS 1.2 (0x0303)
                    [Expert Info (Chat/Deprecated): This legacy_version field MUST be ignored. The supported_versions extension is present and MUST be used instead.]
                Random: d9048e4df69fb33558be6fa3cd96fe435555808701d084c47a32def7770015a0
                Session ID Length: 0
                Cipher Suites Length: 6
                Cipher Suites (3 suites)
                Compression Methods Length: 1
                Compression Methods (1 method)
                Extensions Length: 726
                Extension: key_share (len=268) secp256r1, secp384r1, x25519, x448
                    Type: key_share (51)
                    Length: 268
                    Key Share extension
                Extension: supported_versions (len=3) TLS 1.3
                    Type: supported_versions (43)
                    Length: 3
                    Supported Versions length: 2
                    Supported Version: TLS 1.3 (0x0304)
                Extension: signature_algorithms (len=20)
                    Type: signature_algorithms (13)
                    Length: 20
                    Signature Hash Algorithms Length: 18
                    Signature Hash Algorithms (9 algorithms)
                Extension: supported_groups (len=10)
                    Type: supported_groups (10)
                    Length: 10
                    Supported Groups List Length: 8
                    Supported Groups (4 groups)
                Extension: psk_key_exchange_modes (len=2)
                    Type: psk_key_exchange_modes (45)
                    Length: 2
                    PSK Key Exchange Modes Length: 1
                    PSK Key Exchange Mode: PSK with (EC)DHE key establishment (psk_dhe_ke) (1)
                Extension: server_name (len=24) name=cloudflare-quic.com
                    Type: server_name (0)
                    Length: 24
                    Server Name Indication extension
                Extension: application_layer_protocol_negotiation (len=5)
                    Type: application_layer_protocol_negotiation (16)
                    Length: 5
                    ALPN Extension Length: 3
                    ALPN Protocol
                Extension: quic_transport_parameters (len=71)
                    Type: quic_transport_parameters (57)
                    Length: 71
                    Parameter: max_idle_timeout (len=4) 60000 ms
                    Parameter: initial_max_data (len=4) 1048576
                    Parameter: initial_max_stream_data_bidi_local (len=4) 1048576
                    Parameter: initial_max_stream_data_bidi_remote (len=4) 1048576
                    Parameter: initial_max_stream_data_uni (len=4) 1048576
                    Parameter: initial_max_streams_bidi (len=2) 128
                    Parameter: initial_max_streams_uni (len=2) 128
                    Parameter: ack_delay_exponent (len=1)
                    Parameter: max_ack_delay (len=1) 25
                    Parameter: active_connection_id_limit (len=1) 8
                    Parameter: initial_source_connection_id (len=8)
                    Parameter: version_information (len=12)
                Extension: early_data (len=0)
                    Type: early_data (42)
                    Length: 0
                Extension: pre_shared_key (len=283)
                    Type: pre_shared_key (41)
                    Length: 283
                    Pre-Shared Key extension
                [JA4: q13d0310h3_55b375c5d22e_43a52939c45c]
                [JA4_r: q13d0310h3_1301,1302,1303_000a,000d,0029,002a,002b,002d,0033,0039_0403,0804,0401,0503,0805,0501,0201,0807,0808]
                [JA3 Fullstring: 771,4866-4865-4867,51-43-13-10-45-0-16-57-42-41,23-24-29-30,]
                [JA3: 03a7d247df95a12cc70c33a4bae548bf]
QUIC IETF
    [Expert Info (Note/Protocol): (Random) padding data appended to the datagram]


可能用到的东西：
1. 每类实验的执行命令
  这个一定要记，后面写“实验步骤”直接能用。

  TLS 1.2

  openssl s_client -connect tls-v1-2.badssl.com:1012 -servername tls-v1-2.badssl.com -tls1_2 -sess_out tls12_sess.pem
  -msg
  openssl s_client -connect tls-v1-2.badssl.com:1012 -servername tls-v1-2.badssl.com -tls1_2 -sess_in tls12_sess.pem
  -msg

  TLS 1.3

  openssl s_client -connect www.cloudflare.com:443 -servername www.cloudflare.com -tls1_3 -sess_out tls13_sess.pem -msg
  openssl s_client -connect www.cloudflare.com:443 -servername www.cloudflare.com -tls1_3 -sess_in tls13_sess.pem -msg

  QUIC

  Remove-Item .\quic.ticket -ErrorAction SilentlyContinue
  python .\examples\http3_client.py -v -l quic_new.keys -s quic.ticket https://cloudflare-quic.com/
  python .\examples\http3_client.py -v -l quic_resume.keys -s quic.ticket https://cloudflare-quic.com/

  2. 每次抓包的过滤器
  后面写“抓包方法”会很方便。

  例如：

  TLS 1.2

  ip.addr == 104.154.89.105 and tcp.port == 1012

  TLS 1.3

  ip.addr == 104.16.124.96 and tcp.port == 443

  QUIC

  ip.addr == 104.18.26.14 and udp.port == 443

  3. 每部分的握手顺序
  不要只放截图，直接写成一行。

  例如：

  TLS 1.2 新会话

  Client Hello -> Server Hello -> Certificate -> Server Key Exchange -> Server Hello Done -> Client Key Exchange ->
  Change Cipher Spec -> Finished

  TLS 1.2 恢复

  Client Hello -> Server Hello -> Change Cipher Spec -> Encrypted Handshake Message

  TLS 1.3 新会话

  Client Hello -> Server Hello -> Change Cipher Spec -> Application Data

  TLS 1.3 恢复

  Client Hello(pre_shared_key) -> Server Hello(pre_shared_key) -> Change Cipher Spec -> Application Data

  QUIC 新连接

  Initial -> Handshake -> Protected Payload

  QUIC 恢复连接

  Initial(pre_shared_key, early_data) -> 简化后的后续握手

  4. 每部分的“判定依据”
  这个最重要，后面写分析时直接抄。

  例如：

  - TLS 1.2 新会话：出现 Certificate、Server Key Exchange、Server Hello Done
  - TLS 1.2 恢复：无 Certificate、无 Server Key Exchange，且 Client Hello 带 session_ticket
  - TLS 1.3 新会话：Client Hello 无 pre_shared_key
  - TLS 1.3 恢复：Client Hello 和 Server Hello 出现 pre_shared_key
  - QUIC 新连接：Client Hello 无 pre_shared_key
  - QUIC 恢复连接：Client Hello 出现 pre_shared_key，并带 early_data

  5. 每部分只保留关键字段
  建议固定成这几个，别太多：

  Client Hello

  - Version
  - Random
  - Session ID
  - Cipher Suites
  - 关键 Extensions

  Server Hello

  - Version
  - Random
  - Session ID
  - Cipher Suite
  - 关键 Extensions

  6. 截图和文字做对应
  比如在每节末尾加一句：

  对应截图：TLS1-2.png
  对应截图：TLS1-3.png
  对应截图：QUIC_new.png
  对应截图：QUIC_reconnect.png

  7. 统一编码
  你现在 record.md 已经有乱码了。后面一定要：

  - 统一保存为 UTF-8