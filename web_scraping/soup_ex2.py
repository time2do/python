# BeautifulSoup 모듈 사용하기

from bs4 import BeautifulSoup

html_str = """
<html>
<body>
    <ul class = 'item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로   봇</li>
    </ul>
        <ul class = 'lang'>
        <li>영어</li>
        <li>한국어</li>
        <li>중국어</li>
    </ul>
</body>
</html>
"""

contents = BeautifulSoup(html_str, 'html.parser')
ul = contents.find('ul', {'class': 'lang'})  # item이 lang인 ul 를 찾기
# print(ul)

# li = ul.find('li')  이렇게 하면 첫번째줄만 나옴
# print(li)

# 중국어 찾고 싶을때

lis = ul.find_all('li')
print(lis)
print(lis[2].text)