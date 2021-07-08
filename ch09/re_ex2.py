# {m} m은 반복 횟수

import re

str = "123?45yy7890 hi 999 Hello"
m1 = re.findall("\d{1,3}", str)
print(m1)

m2 = re.findall("[A-z]+", str) # '+'는 반복,단어로 출력. '+' 안 쓰면 철자만 출력
print(m2)

m3 = re.findall("[1-5]{1,2}", str)
print(m3)