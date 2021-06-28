#로또 번호 생성

import random as r
'''
lotto = []


for x in range(6):
    n = r.randint(1,45)
    if n not in lotto:
        lotto.append(n)

    
    
print(lotto)
'''

lotto2 = []
while len(lotto2) <6: #6자리 될때 까지 반복
    n = r.randint(1,45)  # 1~45 까지 난수 랜덤
    if n not in lotto2:   #위에 생성된 숫자가 lotto2에 없으면
        lotto2.append(n)  #lotto2 리스트에 넣기
print(lotto2)
