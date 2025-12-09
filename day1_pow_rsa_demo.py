import hashlib
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii


def pow_mining(nickname, leading_zeros):
    """
    POW 挖矿函数
    :param nickname: 你的昵称
    :param leading_zeros: 需要的前导零个数
    :return: nonce, hash_content, hash_value, elapsed_time
    """
    nonce = 0
    target_prefix = '0' * leading_zeros
    start_time = time.time()

    while True:
        # 组合昵称和nonce
        hash_content = f"{nickname}{nonce}"

        # 计算SHA256哈希值
        hash_value = hashlib.sha256(hash_content.encode('utf-8')).hexdigest()

        # 检查是否满足条件
        if hash_value.startswith(target_prefix):
            end_time = time.time()
            elapsed_time = end_time - start_time
            return nonce, hash_content, hash_value, elapsed_time

        nonce += 1


def generate_rsa_keypair(key_size=2048):
    """
    生成 RSA 公私钥对
    :param key_size: 密钥长度，默认 2048 位
    :return: private_key, public_key
    """
    print("=" * 80)
    print("【步骤 1】生成 RSA 公私钥对")
    print("-" * 80)

    # 生成密钥对
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()

    print(f"✓ 成功生成 {key_size} 位 RSA 密钥对")
    print(f"\n私钥信息:")
    print(f"  - 密钥长度: {key_size} 位")
    print(f"  - 模数 n: {private_key.n}")
    print(f"  - 公钥指数 e: {private_key.e}")
    print(f"  - 私钥指数 d: {private_key.d}")

    print(f"\n公钥信息:")
    print(f"  - 密钥长度: {key_size} 位")
    print(f"  - 模数 n: {public_key.n}")
    print(f"  - 公钥指数 e: {public_key.e}")

    # 导出 PEM 格式
    private_pem = private_key.export_key().decode('utf-8')
    public_pem = public_key.export_key().decode('utf-8')

    print(f"\n私钥 (PEM 格式):")
    print(private_pem)

    print(f"\n公钥 (PEM 格式):")
    print(public_pem)

    return private_key, public_key


def sign_message(private_key, message):
    """
    使用私钥对消息进行签名
    :param private_key: RSA 私钥
    :param message: 要签名的消息
    :return: signature (签名)
    """
    print("\n" + "=" * 80)
    print("【步骤 3】使用私钥进行数字签名")
    print("-" * 80)

    # 对消息进行 SHA256 哈希
    message_hash = SHA256.new(message.encode('utf-8'))

    # 使用私钥签名
    signature = pkcs1_15.new(private_key).sign(message_hash)

    print(f"✓ 签名成功")
    print(f"原始消息: {message}")
    print(f"消息哈希: {message_hash.hexdigest()}")
    print(f"签名 (hex): {binascii.hexlify(signature).decode('utf-8')}")
    print(f"签名长度: {len(signature)} 字节")

    return signature


def verify_signature(public_key, message, signature):
    """
    使用公钥验证签名
    :param public_key: RSA 公钥
    :param message: 原始消息
    :param signature: 签名
    :return: True/False
    """
    print("\n" + "=" * 80)
    print("【步骤 4】使用公钥验证签名")
    print("-" * 80)

    try:
        # 对消息进行 SHA256 哈希
        message_hash = SHA256.new(message.encode('utf-8'))

        # 使用公钥验证签名
        pkcs1_15.new(public_key).verify(message_hash, signature)

        print(f"✓ 签名验证成功！")
        print(f"验证消息: {message}")
        print(f"消息哈希: {message_hash.hexdigest()}")
        print(f"签名 (hex): {binascii.hexlify(signature).decode('utf-8')}")
        print(f"\n结论: 该消息确实由私钥持有者签名，未被篡改！")

        return True
    except (ValueError, TypeError) as e:
        print(f"✗ 签名验证失败！")
        print(f"错误信息: {e}")
        print(f"\n结论: 消息可能被篡改或签名无效！")
        return False


def save_keys_to_file(private_key, public_key):
    """
    将密钥保存到文件
    """
    # 保存私钥
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.export_key())

    # 保存公钥
    with open('public_key.pem', 'wb') as f:
        f.write(public_key.export_key())

    print(f"\n✓ 密钥已保存到文件:")
    print(f"  - 私钥: private_key.pem")
    print(f"  - 公钥: public_key.pem")


def main():
    # 设置昵称
    nickname = "Achang"  # 修改为你的昵称

    print("=" * 80)
    print("POW + RSA 非对称加密演示")
    print("=" * 80)
    print(f"昵称: {nickname}\n")

    # 步骤 1: 生成 RSA 公私钥对
    private_key, public_key = generate_rsa_keypair(key_size=2048)

    # 保存密钥到文件
    save_keys_to_file(private_key, public_key)

    # 步骤 2: POW 挖矿，找到 4 个 0 开头的哈希值
    print("\n" + "=" * 80)
    print("【步骤 2】POW 挖矿 - 寻找 4 个 0 开头的哈希值")
    print("-" * 80)

    nonce, hash_content, hash_value, elapsed_time = pow_mining(nickname, 4)

    print(f"✓ 找到了!")
    print(f"花费时间: {elapsed_time:.4f} 秒")
    print(f"Nonce 值: {nonce}")
    print(f"Hash 内容: {hash_content}")
    print(f"Hash 值: {hash_value}")
    print(f"尝试次数: {nonce + 1} 次")

    # 步骤 3: 使用私钥对 "昵称 + nonce" 进行签名
    message = hash_content  # 即 "kingstarling12345" 这样的格式
    signature = sign_message(private_key, message)

    # 步骤 4: 使用公钥验证签名
    is_valid = verify_signature(public_key, message, signature)

    # 额外测试：验证篡改后的消息
    print("\n" + "=" * 80)
    print("【额外测试】验证篡改后的消息")
    print("-" * 80)

    tampered_message = hash_content + "tampered"
    print(f"篡改后的消息: {tampered_message}")
    verify_signature(public_key, tampered_message, signature)

    # 总结
    print("\n" + "=" * 80)
    print("【总结】")
    print("=" * 80)
    print(f"1. 生成了 2048 位 RSA 公私钥对")
    print(f"2. 通过 POW 找到了满足条件的哈希值: {hash_value}")
    print(f"3. 使用私钥对 '{message}' 进行了数字签名")
    print(f"4. 使用公钥成功验证了签名的有效性")
    print(f"5. 验证了篡改消息后签名验证会失败")
    print("=" * 80)

    print("\n✓ 演示完成！")


if __name__ == "__main__":
    main()
