with open("2021kbo.txt", 'w') as f:
    team = ['삼성', 'LG', '기아', '롯데']
    for i in team:
        f.write(i + '\n')

with open("2021kbo.txt", 'r') as f:
    '''
    data = f.readlines()  # 리스트로 변환
    print(data)
    for i in range(4):
        data = f.readline().split()
        print(data)
'''
    #이차원리스트 만들기
    d2=[]
    for i in range(4):
        d2.append(f.readline().split())
    print(d2)