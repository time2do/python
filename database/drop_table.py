#테이블 삭제

from libs.db.dbconn import getconn

def drop_table():
    conn = getconn()  # 네트워크(DB) 연결 객체
    cur = conn.cursor()

    # 테이블 삭제 - SQL DDL(데이터 정의어)
    sql = "drop table member"  # member 테이블을 삭제 하겠다
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()