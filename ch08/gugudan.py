# 파일에 구구단 쓰기

with open('99.txt','w') as f:
    for i in range(2, 10):
        for j in range(1,10):
            gugudan = "%d x %d = %d" % (i, j, i*j)