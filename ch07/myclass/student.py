class Student:
    def __init__(self, sid, name):
        self.sid = sid # 학번
        self.name = name
    def showinfo(self): #정보 출력 함수, 밑에서 반복해서 안 써두 됨
        print(self.sid, self.name)

if __name__ == "__main__": # 여기서만 실행됨
    s1 = Student(1001,"김홍길")
    s1.showinfo()

    s2 = Student(1002,"양대양")
    s2.showinfo()