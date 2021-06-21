#자리 배치도 프로그램

customer_num = int(input("입장객 수 입력: "))
col_num = int(input("좌석 열의 수 입력: "))

if customer_num % col_num == 0:
    row_num = int(customer_num / col_num)
else:
    #row_num = int(customer_num / col_num + 1)
    row_num = customer_num // col_num + 1
    #파이썬에선 //치면 바로 몫이 나온다. int안써두 
#print("%d개의 줄이 필요합니다." %row_num)

print("자리 배치도")
for i in range(0 , row_num): 
    for j in range(1, col_num+1):
        seat_num = i*col_num+j
        print(seat_num , end=' ')
        if seat_num == customer_num: #좌석수가 입장객 수랑 같을때까지 입력
            break
    print()
#range는 숫자 0부터 시작 
