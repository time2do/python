#실시간 주가 가격확인

from urllib import request
from bs4 import BeautifulSoup

def getcontent():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    html = request.urlopen(url)
    contents = BeautifulSoup(html, 'html.parser')
    return contents

cont = getcontent()
no_today = cont.find('p', {'class': 'no_today'})
#print(no_today)

price = no_today.find('span',{'class': 'blind'})
print(price)
print("삼성전자 주가: {}원".format(price.text))