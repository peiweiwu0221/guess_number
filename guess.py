import random
r = random.randint(1, 100)
i = 1
while True:
    guess = int(input('請輸入1到100內的數字:'))
    if r == guess:
        print('猜對了，恭喜你')
        break
    else:
        print('猜錯了，請再次嘗試')
        if guess > r:
            print('數字比您猜的還要小')
        else:
            print('數字比您猜的還要大')
        print('這是您猜的第', i,'次')
        i = i + 1




