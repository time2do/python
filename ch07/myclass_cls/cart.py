# 장바구니에 물건 담기 - 같은 장바구니에 추가되지않음

class Cart:
    def __init__(self,goods):
        self.li = [] #빈 리스트 만들기
        self.li.append(goods) #goods를 추가하기

    def showinfo(self):
        print(self.li)

cart1 = Cart("커피")
cart1.showinfo()

cart2 = Cart("음료")  # 커피는 사라지고 음료가 추가됨
cart2.showinfo()