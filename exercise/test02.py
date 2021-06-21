

# 1번


sub1 = 80
sub2 = 75
sub3 = 55

sum = sub1 + sub2 + sub3

print(sum/3)


# 2번(자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법)

#print( 13 % 2)

n = 13
if n % 2==0:
    print("짝수")
else:
    print("홀수")
        

# 3번(주민번호를 연월일 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자)

pin= "881120-1068234"
yyyymmdd = pin[:6]
num= pin[7:]
print(yyyymmdd)
print(num)

# 4번(주민번호 성별을 나타내는 숫자를 출력)

pin= "881120-6068234"

gender = int(pin[7])  #int는 연산해야 되면 무조건 붙여줘야 함. 

print(gender)

if gender == 1:
    print("성별은 남자입니다.")
elif gender == 2:
    print("성별은 여자입니다.")
else:
    print("외국인입니다")

# 5번

a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# 6번

a = [1,3,5,4,2]
a.sort()  #오름차순 정렬
print(a)
a.reverse() #내림차순 정렬
print(a)

# 7번
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# split() 예제(공백을 기준으로 문자를 나눔)
msg = 'Life is too short'
msg = msg.split() #구분 기호가 공백
print(msg)

s = "a:b:c:d"
s = s.split(':')  # ':'를 기준으로 나뉘어진
print(s)
