# 조건: 나이가 15세 이상이면 '드라마 관람가', 아니면 '드라마 불가' 출력

age = int(input("나이를 입력하세요: "))

if age >= 15:
    print("드라마 관람가")
else:
    print("드라마 불가")

print("나이는 %d세입니다" % age)
