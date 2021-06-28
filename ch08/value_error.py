while True:
    try: #문자를 입력하면 에러 나니까 try 해줌
        x = int(input("숫자를 입력하세요: "))
        print(x)
        break
    except ValueError: #문자 이외꺼 입력시 ValueError 뜰때 아래 문구가 뜸.
        print("숫자가 아닙니다. 다시 입력하세요.")