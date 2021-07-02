# 웹 스크레이핑(크롤링)

from urllib import request

content = request.urlopen("http://www.naver.com")
print(content.read())