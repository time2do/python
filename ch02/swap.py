#변수값 교환

blue =1
red =2
print("교환전:")
print("blue=",blue,"red=",red)

#교환처리

yellow = blue  #blue를 yellow에 넣기,blue값은 없음,yellow값은 1
blue = red  #red=2를 blue1에 넣기,blue = 2
red = yellow #yellow=1를 red에 넣으면 red는 1이 

print("교환후:")
print("blue=",blue,"red=",red)
