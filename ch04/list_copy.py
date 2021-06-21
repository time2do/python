a = [1, 2, 3, 4, 5, 6]

a2= []  #빈 리스트 하나 만들기

for i in a:
    a2.append(i)
print(a2)

#a 리스트의 홀수를 a3 리스트에 저장

a3 = []

for i in a:
    if i % 2 != 0:
        a3.append(i)
print(a3)
