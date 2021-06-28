import turtle as t
import random as r

t.shape('turtle')
t.speed(0)
t.bgcolor('pink')
#t.setup(500,500) #작업영역(무대)의 크기

for x in range(100):  #백번 움직임
    angle = r.randint(1,360)    #각도는 360도
    t.setheading(angle) #거북이의 방향
    t.forward(50)

t.mainloop()