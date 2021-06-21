#4년에 한번 윤년이나 100년에 한번 윤년아니다. 혹은 400으로 나눠질때 윤년이다.

year = int(input("연도를 입력하세요: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
    print("윤년입니다")
else:
    print("%d년은 윤년이 아닙니다." % year)
