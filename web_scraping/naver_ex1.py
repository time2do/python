#네이버에서 원하는 태그 찾기

from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://www.naver.com/")
contents = BeautifulSoup(html, 'html.parser')

div = contents.find('div', {'class': 'service_area'})
a = div.find('a')
print(a)
print(a.text)