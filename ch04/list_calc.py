#리스트의 연산

score = [70, 80, 50, 60, 90, 40]
sum = 0
count = len(score)   #len은 개수


for i in score:
    sum += i
    print("i=%d, sum=%d" % (i,sum))  #합계과정 출력

    
print("개수: %d개" % count)

print("합계: %d점" % sum)

avg = sum / count
print("평균: %.1f점" % avg)  # .1f 하면 소수점 첫째자리까지 나
