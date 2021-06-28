import random

for i in range(10):  # 주사위 10번 던지기
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    total = dice1 + dice2
    print(dice1,dice2)
    if total == 7:
        print('Seven Thrown!!')
    if total == 11:
        print('Eleven Thrown!!')
    if dice1 == dice2:
        print('Double Thrown!!')
