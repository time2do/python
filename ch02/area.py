#정사각형의 넓이

size= int(input("한 변의 길이: "))   #int를 안 써주면 문자로 인식함
area = size*size
#print("정사각형의 넓이: ",area,"cm") 이렇게 하면 숫자와 cm이 띄어쓰기 됨
print("정사각형의 넓이: %dcm" % area)  #숫자와 cm 붙여쓰기

#삼각형의 넓이

width = int(input("밑 변의 길이: "))
height = int(input("높이의 길이: "))
area = (width * height)/2

print("삼각형의 넓이: %dcm" % area)
