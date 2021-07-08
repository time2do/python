def gugu(dan):
    li = []
    for i in range(1, 10):
        li.append(dan * i)
    return li

dan_2 = gugu(2)
print(dan_2)

'''

user_input = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
gugu = int(user_input)
for i in range(1,10):
    print(i*gugu, end=' ')

'''