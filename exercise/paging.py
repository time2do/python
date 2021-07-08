# x // y 하면 몫만 나옴  5 나누기 3 하면 1만 나옴
# 10의 배수는 페이지 넘어 가지 않아야 함

def getpage(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1  # 몫이 0일때 있어서 +1 해줘야 함


print(getpage(5, 10))
print(getpage(10, 10))
print(getpage(15, 10))
print(getpage(20, 10))
print(getpage(25, 10))
