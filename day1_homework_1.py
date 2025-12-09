import hashlib
import time


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


def main():
    # 请在这里修改为你自己的昵称
    nickname = "Achang"  # 修改为你的昵称

    print("=" * 80)
    print("POW (Proof of Work) 工作量证明演示")
    print("=" * 80)
    print(f"昵称: {nickname}\n")

    # 挑战1: 4个0开头
    print("【挑战 1】寻找 4 个 0 开头的哈希值...")
    print("-" * 80)
    nonce1, content1, hash1, time1 = pow_mining(nickname, 4)
    print(f"✓ 找到了!")
    print(f"花费时间: {time1:.4f} 秒")
    print(f"Nonce 值: {nonce1}")
    print(f"Hash 内容: {content1}")
    print(f"Hash 值: {hash1}")
    print(f"尝试次数: {nonce1 + 1} 次\n")

    # 挑战2: 5个0开头
    print("【挑战 2】寻找 5 个 0 开头的哈希值...")
    print("-" * 80)
    nonce2, content2, hash2, time2 = pow_mining(nickname, 5)
    print(f"✓ 找到了!")
    print(f"花费时间: {time2:.4f} 秒")
    print(f"Nonce 值: {nonce2}")
    print(f"Hash 内容: {content2}")
    print(f"Hash 值: {hash2}")
    print(f"尝试次数: {nonce2 + 1} 次\n")

    # 难度对比
    print("=" * 80)
    print("【难度对比】")
    print("-" * 80)
    print(f"4个0: 尝试 {nonce1 + 1} 次, 耗时 {time1:.4f} 秒")
    print(f"5个0: 尝试 {nonce2 + 1} 次, 耗时 {time2:.4f} 秒")
    print(f"难度提升: {(nonce2 + 1) / (nonce1 + 1):.2f} 倍")
    print(f"时间提升: {time2 / time1:.2f} 倍")
    print("=" * 80)


if __name__ == "__main__":
    main()
