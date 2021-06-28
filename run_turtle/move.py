# 거북이 랜덤 장소에 출현

import turtle as t
import random


t.shape('turtle')
t.speed(0)
t.up()  #선을 없애기
#t.goto(200,0)

x = random.randint(-230,230)
y = random.randint(-230,230)
t.goto(x,y)




t.mainloop()