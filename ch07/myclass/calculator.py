class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

# 아래껀 여기서만 할때 씀
if __name__ == "__main__":
    cal = Calculator(x,y)
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())