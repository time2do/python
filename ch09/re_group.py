import re

p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")
s = p.search("jang 010-1234-5678")
print(s.group(1))
print(s.group(2))