# 특정한 회원 검색하기

from libs.db.dbconn import getconn

def select_one():
    conn = getconn()
    cur = conn.cursor()
    #1명 검색 SQL
    sql = "select * from member where mem_num = 103 "
    cur.execute(sql)
    print("회원번호로 검색")

    rs = cur.fetchone()

    print(rs)
    conn.close()

if __name__ == "__main__":
    select_one()