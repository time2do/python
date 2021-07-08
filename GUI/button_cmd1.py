from tkinter import *

def click():
    print("Hello~ Python!!")

root = Tk()
root.title("Hello~")
root.geometry("400x100+700+400")

frame = Frame(root)  # root 위에 위치하는 프레임 객체
frame.pack()  # 레이아웃 담당하는 팩 메서드

Button(frame, text="확인", command=click).grid(row=0, column=0)
# click 뒤에 ()를 빼는 이유는 버튼 누를때만 함수가 발생해야 하는데 ()를 넣으면 바로 실행됨



root.mainloop()