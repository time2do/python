import random

'''
# 주사위 10번 던지기

dice =[]
for i in range(0,10):
    n = random.randint(1, 6)  # 1부터 6까지 나옴
    dice.append(n) # 리스트에 담을때

print(dice)
'''

# 로또 복권 생성기

lotto = []
'''
for i in range(6): #for 문 쓰면 중복된 숫자 안나오므로 숫자 5개만 나옴, 그래서 while문 써야함
    n = random.randint(1, 45)
    if n not in lotto: # 중복 숫자 방지
        lotto.append(n)
print(lotto)
'''
while len(lotto) < 6:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

print(lotto)