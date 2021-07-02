# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()  # db연결
    cur = conn.cursor()
    # 자료 추가 - SQL

    cur.execute("insert into member values ('태진이',43)") #수정하면 db에 추가됨
    cur.execute("insert into member values ('이핑크',14)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()