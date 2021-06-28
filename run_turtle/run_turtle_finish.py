import turtle as t
import random

def turn_right(): #오른쪽 화살키
    t.setheading(0) #수평

def turn_up():
    t.setheading(90) #각도가 90도

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()  #글짜가 사라짐
        play()

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))
    t.home()

def play():
    global score
    global playing

    t.forward(10) #주인공 거북이 속도

    #적 거북이의 속도는 점수가 올라가면 1씩 증가

    if random.randint(1,5) == 3:  #3을 뽑을 확률이 20%
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)  #적 거북이 속도

    #주인공이 먹이를 먹으면 점수가 1 올라감
    if t.distance(tf) < 12:
        score += 1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)

    #주인공 거북이가 적에게 잡히면 게임 종료
    if t.distance(te)<12:
        text = "Score: " + str(score)
        message("Game Over",text)
        playing = False
        score = 0

    if playing:
        t.ontimer(play,100)

# 메인 영역
#점수 변수와 플레이 스위치(bool) 변수 선언

score = 0
playing = False

t.setup(500,500)
t.title("달려라 거북이")
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white") #주인공은 흰색

#적 거북이
te = t.Turtle() # Turtle() 클래스에서 te 인스턴스 생성
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

# 먹이

tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0,-200)

#키보드 작동

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start,"space")
t.listen()
message("Turtle Run","[Space]")

t.mainloop()