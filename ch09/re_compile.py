# 정규 표현식 예제

import re
# re.compile 정규표현식 저장하기

p = re.compile('[a-z]+')  # '+'는 반복을 의미하는 메타 문자
m = p.match('aaaab')  #match는 첫번째꺼만 찾아줌

print(m)
print(m.group())  # group()은 문자열을 표시해주는 함수



