count = 3
while count > 0:
    temp = input("猜猜我心里想的什么数字")
    guess = int(temp)
    if guess == 8:
        print("你真的厉害")
        break
    else:
        if guess > 8:
            print("猜的有点大了")
        else:
            print("猜的有点小了")
    count = count - 1
print("游戏结束")
