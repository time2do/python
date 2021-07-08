# 주민번호 뒷자리 *처리
# re.compile 정규표현식 저장하기
import re

data = """
    kim 860123-1542589
    lee 951011-2345678
"""

pat = re.compile("(\d{6})[-]\d{7}")  # 주민번호 앞자리 6, 뒷자리 7
m = pat.sub("\g<1>-*******", data)  # 앞자리 그대로 뒷자리만 별표처리
print(m)