# 중첩 for 

# 5행 5열의 배열

for i in range(0,5): #혹은 range(1,6)
    for j in range(0,5):  #혹은 range(1,6)
        print("가", end=' ')
    print()
    
print()

# 1부터 1씩 증가하기
for i in range(0,5): #혹은 range(1,6)
    for j in range(1,6): # range(0,5)로 하면 0부터 찍힘
        print(j, end=' ')
    print()
    
print()

for i in range(0,6): #혹은 range(1,6)
    for j in range(1,6): # range(0,5)로 하면 0부터 찍힘
        num = i *  5 + j
        if i < 2:
            print(num, end='   ')  #첫두줄은 세번씩 띄어쓰기
        else:
            print(num, end=' ')
        
    print()
