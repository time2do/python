# 여러개의 원 만들기
import turtle as t

t.speed(0)
t.color('yellow')
t.bgcolor('black')
n = 50
for x in range(n):
    t.circle(80)
    t.left(360/n)

t.mainloop()