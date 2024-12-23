# 从1到100的猜数游戏
import random

num = random.randrange(1, 100)

sign = True
start = 1
stop = 100
print("退出请输入：/q")
while sign:
    str_start = str(start)
    str_stop = str(stop)
    message = "请输入从" + str_start + "到" + str_stop + "以内的一个数："
    guess = input(message)
    if guess == '/q':
        sign = False
    elif int(guess) == num:
        print("恭喜你！猜对了！")
        num = random.randrange(1, 100)
        start = 1
        stop = 100
    elif int(guess) > num:
        print("过大")
        if stop > int(guess):
            stop = int(guess)
    elif int(guess) < num:
        print("过小")
        if start < int(guess):
            start = int(guess)
