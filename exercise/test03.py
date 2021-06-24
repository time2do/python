# 1번

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")
    

# 2번= 1부터 천까지의 자연수 중 3의 배수의 합을 구하기

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)


# 3번

i = 0
while True:
    i += 1
    if i > 5:
        break
    print(i*'*')

# 2중 for문

for i in range(1, 6):
    for j in range(1, i+1):
        print('*',end=' ')
    print()

# 4번 - for문을 사용해 1부터 100까지의 숫자를 출력해 보자

for i in range(1,101):
    print(i)

# 5번 - A학급에 총 10명의 학생이 있다. for문을 사용하여 평균 점수를 구하라

A=[70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

# 6번 - 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드를 리스트 내포를 사용하여 표현하라
'''
numbers = [1,2,3,4,5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)
'''
#리스트 내포
numbers = [1,2,3,4,5]

result = [n*2 for n in numbers if n%2==1]

print(result)

