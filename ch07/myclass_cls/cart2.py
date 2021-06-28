# 클래스 변수 사용 - 장바구니에 추가됨
class Cart:
    li = []  #클래스 변수 생성
    def __init__(self,goods):
        Cart.li.append(goods)  # 클래스 함수중 li변수에 goods요소를 추가

    def showinfo(self):
        print(self.li)

cart1 = Cart("커피")
cart1.showinfo()

cart2 = Cart("음료")  # 커피에 음료가 추가됨
cart2.showinfo()

cart3 = Cart("우유")
cart3.showinfo()