# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()  # db연결
    cur = conn.cursor()
    # 자료 추가 - SQL

    cur.execute("insert into member values (103, '이도룡',24)") #수정하면 db에 추가됨
    cur.execute("insert into member values (105, '황해',55)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()