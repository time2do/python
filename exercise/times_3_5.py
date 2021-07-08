# 3과 5의 배수의 합

sum = 0
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        print(i)

print("3과 5의 배수의 합은 %s입니다" %sum)