#다중 에러 처리

try:
    a = [1, 2]
    #print(a[2])

    4 / 0

except IndexError:
    print("범위에 있지 않습니다.")

except ZeroDivisionError:
    print("0으로 나눌수 없습니다.")

"""
except ZeroDivisionError as e:
    print(e)
"""