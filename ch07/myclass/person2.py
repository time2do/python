# 여러명 가능

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("박대양",40)
print(p1.name, p1.age)
p2 = Person("이산",25)
print(p2.name, p2.age)