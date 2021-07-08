from tkinter import *


def click():
    en_text = entry.get()
    text.delete(0.0, END)
    text.insert(END, en_text)  # END는 최종 입력 지점


root = Tk()
root.title("Hello~")
root.geometry("200x150+700+400")

frame = Frame(root)  # root 위에 위치하는 프레임 객체
frame.pack()  # 레이아웃 담당하는 팩 메서드

Label(frame, text="이름: ").grid(row=0, column=0)

entry = Entry(frame, width=10)
entry.grid(row=0, column=1)  # Label이랑 같은 행이고 두번째열
Button(frame, text="확인", command=click).grid(row=1, columnspan=2)  # columnspan 두개 합치기
# click 뒤에 ()를 빼는 이유는 버튼 누를때만 함수가 발생해야 하는데 ()를 넣으면 바로 실행됨

text = Text(frame, width=20, height=5)
text.grid(row=2, columnspan=2)

root.mainloop()