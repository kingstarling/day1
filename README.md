# POW (Proof of Work) 工作量证明演示

这是一个简单的 POW 算法实现，通过不断尝试 nonce 值来寻找满足特定条件的 SHA256 哈希值。

## 功能说明

- 使用昵称 + nonce 进行 SHA256 哈希运算
- 寻找 4 个 0 开头的哈希值
- 寻找 5 个 0 开头的哈希值
- 统计并对比挖矿时间和难度

## 环境要求

- Python 3.6+
- 无需额外依赖库（使用标准库）

## 使用方法

1. 克隆项目
```bash
git clone https://github.com/你的用户名/pow-demo.git
cd pow-demo
