# 리스트의 최대값, 최소값, 정렬

score = [70, 80, 50, 60, 90, 40]
max = score[0]
min = score[0]
n = len(score)  #6

for i in score:  #이게 더 간편함. 아래꺼보
    if max < i:  #max가 i보다 작을때
        max = i  #max를 i로 바꾸기

print("최고 점수 %d점" % max)

for i in range(1,n):
    if min > score[i]:
        min = score[i]

print("최저 점수 %d점" % min)

#오름차순 정렬


'''
for i in range(0,n):
    for j in range(0, n-1):
        if score[j] > score[j+1]:
            score[j],score[j+1] = score[j+1],score[j]

for i in score:
    print(i, end=' ')
'''

score.sort()
print(score)
