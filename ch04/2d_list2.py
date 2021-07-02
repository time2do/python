#1차원

d1 = [1, 2, 3]
print(d1[0])

d1.append(10)  #d1 리스트에 추가
print(d1)

#2차원

d2 = [
    [10],
    [20],
    [30]
    ]  #3행1열

print(d2[0][0])

d2.append([40])  #[]가 없으면 값이 추가됨
print(d2)

for i in d2:
    print([i][0])

d2.append([d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]])
print(d2)
avg = (d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0])/4
d2.append([avg])
print(d2)