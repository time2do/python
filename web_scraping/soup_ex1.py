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
</body>
</html>
"""

soup = BeautifulSoup(html_str, 'html.parser')
#print(soup)
ul = soup.find('ul') #ul를 찾아라
#print(ul)
print(ul.text) # 글짜만 나옴