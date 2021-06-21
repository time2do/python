# 놀이 공원 입장료 계산

age = int(input("나이를 입력해 주세요: "))
charge = 0

if age < 8:
    print("미취학 아동입니다.")
    charge = 1000
    
elif age < 14:
    print("초등학생 입니다.")
    charge = 2000
elif age < 20:
    print("중고등학생 입니다.")
    charge = 2500
else:
    print("성인 입니다.")
    charge = 3000


print("입장료는 %d원 입니다." % charge)
