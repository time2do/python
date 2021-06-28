# Car는 부모 클래스 - Bus,Taxi는 자식 클래스
# 상속의 경우 - 메서드 재정의가 발생함

class Car:
    def drive(self):
        print("차가 주행합니다.")

class Taxi(Car):
    def drive(self):
        print("택시가 주행합니다.")

class Bus(Car):
    def drive(self):
        print("버스가 주행합니다.")

c = Car()
c.drive()

t = Taxi()
t.drive()

b = Bus()
b.drive()