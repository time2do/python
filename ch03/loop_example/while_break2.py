# while ~ break

while True:  #무한반복
    #print("반복을 계속할까요? [y/n] : ")
    #answer = input()
    answer = input("반복을 계속할까요? [y/n] : ")

    if answer == 'y' or answer == 'Y':
        print("반복을 계속합니다.")
    elif answer == 'n' or answer == 'N':
        print("반복을 중단합니다.")
        break
    else:
        print("잘못된 입력입니다.")
