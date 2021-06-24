# 도형의 면적을 계산하는 함수 정의와 사용


def square(w,h):
    area = w * h
    return area


def triangle(n,h):
    area = n * h / 2
    return area


print('사각형의 면적: ', square(5,4))
print('삼각형의 면적: ', triangle(4,7))
