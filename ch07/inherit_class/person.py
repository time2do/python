# Person 클래스 -  멤버변수(name,age)
# Employee 클래스는 Person을 상속 받음
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    pass   #테스트 할때 pass 넣고 다음에 수정


if __name__ == "__name__":
    p1 = Person("강하늘",25)
    print(p1.name,p1.age)

    e1 = Employee("강하늘",25)
    print(e1.name,e1.age)