# 第一个 Python 脚本
import sys
import datetime

print("Hello, Python!")
print(f"Python 版本: {sys.version.split()[0]}")
print(f"当前时间: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")

# 一个简单的示例：计算 1~100 的和
total = sum(range(1, 101))
print(f"1 + 2 + ... + 100 = {total}")
