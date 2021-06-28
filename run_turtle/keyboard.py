import turtle as t
t.speed(0)

def turn_right(): #오른쪽 화살키
    t.setheading(0) #수평
    t.forward(10)

def turn_up():
    t.setheading(90) #각도가 90도
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear(): #선 지우기
    t.clear()

t.shape("turtle")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, "Escape") #esc 누르면 선 지워짐

t.listen() #키보드의 동작을 기다림

t.mainloop()