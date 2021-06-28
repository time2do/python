# Student 클래스
from person import Person

class Student(Person):
    def __init__(self,name,age,stuId):
        super().__init__(name,age)
        self.stuId = stuId
        
    def showinfo(self):
        print(self.name,self.age,self.stuId)


s1 = Student("김학",27,880303)
s1.showinfo()

s2 = Student("해찬들",26,880808)
s2.showinfo()
