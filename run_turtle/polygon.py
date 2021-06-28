# 다른 곳에 도형 그리기
import turtle as t

t.shape('turtle')

def polygon(n):
    for x in range(n):
        t.forward(100)
        t.left(360/n)
        
def polygon2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)
polygon(5)

t.up() # 선 올리기
t.forward(200)  # 100픽셀만큼 뒤로 이동
t.down() #선 내리기
'''
for x in range(4):
    t.backward(100)
    t.right(90)
'''



polygon2(4,80)
polygon2(5,100)


t.mainloop()