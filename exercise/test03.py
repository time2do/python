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
