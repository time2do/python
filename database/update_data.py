# 자료 내용 변경 - 성춘향을 이몽룡으로 업데이트
from libs.db.dbconn import getconn

def update_data():
    conn = getconn()
    cur = conn.cursor()
    # sql = "update member set name = '이몽룡' where name = '성춘향'"

    # sql = "update member set age = 25 where age = 20"

    # 103번의 이름을 이몽룡으로 변경하기

    sql = "update member set name = '이몽룡' where mem_num = 103"

    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__  == "__main__":
    update_data()