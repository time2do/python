import re

str = "park 010-1234-6789"
pat = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]+\d+)")
# group 으로 할땐 ?P<> 빼야함
'''
m = re.search(pat, str)
print(m.group(0))  # 전체 문자열 반환
print(m.group(1))
print(m.group(2))
'''

# sub 메서드 사용
# s = pat.sub("\g<name> \g<phone>", str)
s = pat.sub("\g<1> \g<2>", str)  # 참조 번호 사용, 위에랑 결과 똑같음, 이때 ?P<>없어도 됨
print(s)