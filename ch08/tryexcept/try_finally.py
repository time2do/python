# try ~ except ~finally

def divide(x, y):
    try:
        div = x / y
        print(div)
    except ZeroDivisionError:
        print("0으로 나눌수 없습니다")
    else:
        print(div)
    finally:
        print("여기는 꼭 수행하는 구간입니다.") #리셋 시킬때

divide(4,0)