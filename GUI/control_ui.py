# 컨트롤 도구 상자 - Label, button, 목록 박스, 입력상자

from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text="제목 ").grid(row=0, column=0)
        Entry(frame, width=20).grid(row=0, column=1)
        Button(frame, text="  확인").grid(row=0, column=2)
        # 체크버튼
        check_var = StringVar()  # 문자형 변수 사용
        check = Checkbutton(frame, text="체크", variable=check_var, onvalue='Y', offvalue='N')
        check.grid(row=1, column=0)
        # 리스트 목록
        listbox = Listbox(frame, height=4, selectmode=SINGLE)  # 여러개 선택은 MULTIPLE
        color = ['red', 'green', 'blue', 'yellow']
        for i in color:
            listbox.insert(END, i)
        listbox.grid(row=1, column=1)
        # 프레임 생성-> 라디오버튼
        radio_frame = Frame(frame)
        radio_sel = StringVar()
        b1 = Radiobutton(radio_frame, text='왼쪽', variable=radio_sel, value='P')
        b1.pack(side=LEFT)
        b1 = Radiobutton(radio_frame, text='오른쪽', variable=radio_sel, value='L')
        b1.pack(side=LEFT)
        radio_frame.grid(row=1, column=2)


root = Tk()
root.title("컨트롤 도구 UI")
app = App(root)




root.mainloop()