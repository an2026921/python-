import sys


def play_game():
    print("=== 猜你心中的数字 ===")
    print("请在心里想一个 1 到 100 之间的整数。")
    print("电脑会来猜，你只需要回答：大了 / 小了 / 对了")
    print("（输入 q 可随时退出）")
    print()

    low, high = 1, 100
    count = 0

    while low <= high:
        guess = (low + high) // 2
        count += 1
        answer = input(f"我猜是 {guess}，对吗？(大/小/对/q)：").strip().lower()

        if answer in ("对", "对了", "是的", "yes", "y", "correct", "="):
            print(f"耶！我用了 {count} 次就猜到了 {guess}！")
            return
        elif answer in ("大", "大了", "太大", "big", "b", ">"):
            high = guess - 1
        elif answer in ("小", "小了", "太小", "small", "s", "<"):
            low = guess + 1
        elif answer == "q":
            print("好的，游戏结束。")
            return
        else:
            print("没看懂，请回答 大 / 小 / 对")
            count -= 1  # 这次不算
    else:
        print("嗯...范围已经没有数字了，你是不是回答错啦？")


if __name__ == "__main__":
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\n游戏已退出。")
        sys.exit(0)
