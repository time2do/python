# Counter 클래스 - 클래스 변수 사용


class Counter:
    x = 0  # 클래스 바로 아래 오는건 클래스 변수

    def __init__(self):

        Counter.x = Counter.x + 1

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()  #1
c2 = Counter()
c2.showinfo()  #2
c3 = Counter()
c3.showinfo()  #3

#x가 초기화 안되므로 계속 증가됨