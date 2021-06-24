# 도형 그리기

import turtle as t   #터틀의 별명은 t

t.shape("turtle")

# 사각형 그리기

for i in range(4):
    t.forward(100)
    t.right(90)
    


# 삼각형 그리기
t.color('red')
t.pensize(2)
for i in range(3):
    t.forward(100)
    t.left(120)
    



# 원
t.color('blue')

n=50 #원 크기

for i in range(4):
    ts = t.circle(n)
    n += 50
    

