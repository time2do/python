import random

com = random.randint(1,30)

while True:
    guess = int(input("맞혀보세요(1~30): "))
    if guess > com:
        print('너무 커요!')
    if guess < com:
        print('너무 작아요!')
    if guess == com:
        print('정답!')
        break
