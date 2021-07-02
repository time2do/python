# 1번 - 책 262p

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value  #요거 안 쓰면 none이 뜸

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

class MaxLimitCalculator(Calculator): # 100 넘을시 100으로 출력
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value


#부모 클래스의 인스턴스

c = Calculator()
print(c.add(10))
print(c.value) #위에 return 안 쓰면 10이 출력 안되고 none 뜸

# 빼기
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(cal2.value)

#4번
'''
def positive(a):
    a2=[]
    for i in li:
        if i >= 0:
            a2.append(i)
    return a2

li = [1, -2, 3, -5, 8, -3]
li2 = positive(li)
print(li2)
'''
li = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x > 0, li)))

#6

li = [1, 2, 3, 4]
print(list(map(lambda x: x*3, li)))

