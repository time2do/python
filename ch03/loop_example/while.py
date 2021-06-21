# while 문: "hello" 10번 반복하기

i = 1
sum = 0
while i < 11:
    
    sum += i
    
    #print(i, end = ' ') #수평 출력
    print("i=", i, ", sum =", sum)
    i += 1

print("합계: " , sum)

#하지만 while 문은 주로 break 랑 같이 씀
