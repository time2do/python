# abs() 직접 정의
#abs 함수는 마이너스를 플러스로 바꿔

def abs_sign(x):
    if x < 0:
        x= -x
    return x

n1 = abs_sign(-5)
print(n1)


