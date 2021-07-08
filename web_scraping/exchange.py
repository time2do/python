from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace')
contents = BeautifulSoup(code, 'html.parser')
div = contents.find('div', {'class': 'market_data'})
lis = div.find_all('li')

for li in lis:
    ex = li.find('span', {'class': 'blind'})  # 환율 종류
    val = li.find('span', {'class': 'value'})  # 환율 가격
    # print(ex.string)
    # print(val.string)
    print(ex.string.split(' ')[-1], ':', val.string)