#global 명령어 사용하기(권장하지 않음)

a = 1
def vartest():
    global a
    a = a + 1

vartest() 
print(a)
