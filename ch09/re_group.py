import re
# \s 는 공백
# 그룹핑된 문자열에 이름 붙이기
# ?P<그룹이름>
p = re.compile("(?P<이름>\w+)\s(?P<전화>\d+[-]\d+[-]\d+)")
s = p.search("jang 010-1234-5678")
print(s.group("이름"))
print(s.group("전화"))