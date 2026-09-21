import random


def play_game():
    target = random.randint(1, 100)
    count = 0
    print("=== 猜数字游戏 ===")
    print("我想了一个 1 到 100 之间的数字，来猜猜看吧！")

    while True:
        guess_text = input("请输入你猜的数字（输入 q 退出）：")
        if guess_text.lower() == "q":
            print(f"正确答案是 {target}，下次再来挑战吧！")
            break

        try:
            guess = int(guess_text)
        except ValueError:
            print("请输入一个有效的数字！")
            continue

        count += 1
        if guess < target:
            print("猜小了，再大一点。")
        elif guess > target:
            print("猜大了，再小一点。")
        else:
            print(f"恭喜你，答对了！答案就是 {target}，你一共猜了 {count} 次。")
            break


if __name__ == "__main__":
    play_game()
