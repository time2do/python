# raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.


class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    #무조건 fly 를 써야 하기 때문에 pass 쓰면 에러 뜸
    #pass
    def fly(self):
        print("독수리가 하늘을 높이 납니다.")

eagle = Eagle()
eagle.fly()
