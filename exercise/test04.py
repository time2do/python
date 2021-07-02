# 1번

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
num = is_odd(5)
print(num)

#2 - 가변 매개변수. 평균값 구하기
# *은 "all"이라는 뜻으로 보면 됨
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
        print(i,result)
    return result / len(args)
print(avg_numbers(1,2,3,4))

'''
#3
input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %s입니다" %total)

#4. - 결과값이 다른것을 찾자
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")  #이렇게 쓰면 띄어쓰기 됨
print("".join(["you","need","python3"]))
'''

#5
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())
f2.close()


#6
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()


#7 - 6번에서 "you need java" 를 입력

f = open('test.txt','r')
body = f.read() #test.txt 파일의 내용을 body 변수에 저장
f.close()

body = body.replace('java','python') #자바를 파이썬으로 변경

f = open('test.txt','w') #파일을 쓰기 모드로 다시 실행
f.write(body)
f.close()

