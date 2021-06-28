# Counter 클래스 - 인스턴스 변수 사용

class Counter:
    def __init__(self):
        self.x = 0 #x변수 초기화(인스턴스 변수)
        self.x = self.x + 1

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()
c2 = Counter()  #위에서 x초기화 하기때문에 답은 변화가 없음
c2.showinfo()
c3 = Counter()
c3.showinfo()