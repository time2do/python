# 멤버 매개변수가 있는 상속
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
'''

#person.py의 Person 클래스 가져오기
from person import Person

class Employee(Person):
    def __init__(self,name,age,empId):
        super().__init__(name,age) #부모꺼 가져오기
        self.empId = empId

    def getname(self):  #캡슐화(정보은닉) - get() 메서드 사용
        return self.name

    def getage(self):
        return self.age

    def getempId(self):
        return self.empId

e1 = Employee("북한산",25,201)
print("이름: ", e1.getname())
print("나이: ", e1.getage())
print("사번: ", e1.getempId())

e2 = Employee("금강산",49,202)
print(e2.name,e2.age,e2.empId)