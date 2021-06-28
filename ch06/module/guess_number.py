import random

com = random.randint(1, 30)

while True:
    try:
        guess = int(input("맞혀보세요(1~30): "))
        if guess > 30 or guess < 1:
            print('범위에 있는 숫자를 입력하세요!')
        elif guess == com:
            print('정답!')
            break
        elif guess > com:
            print('너무 커요!')
        else:
            print('너무 작아요!')

    except ValueError:
        print("숫자가 아닙니다. 다시 입력해주세요!")