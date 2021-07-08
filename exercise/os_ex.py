import os

"""
os.chdir("c:/")
dir = os.popen('dir')
print(dir)
print(dir.read())

"""

# 디렉터리 이름 - 리스트 반환
dirnames = os.listdir("c:/")
print(dirnames)
print(dirnames[0])
print(dirnames[1])
