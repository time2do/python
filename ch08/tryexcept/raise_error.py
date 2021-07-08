# raise -> 에러 미뤄둔다. 사용하는 쪽에서 발생하도록 함
class Bird:
    def fly(self):
        print("새가 날아갑니다.")
        #raise NotImplementedError 에러를 미루기도 하지만 직접 발생도 시킴

class Eagle(Bird):
    #pass
    def fly(self):
        print("독수리가 하늘을 높이 납니다.")

bird = Bird()
bird.fly()

eagle = Eagle()
eagle.fly()