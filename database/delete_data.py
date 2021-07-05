# 특정이나 전체 자료 삭제(테이블 삭제가 아님)
from libs.db.dbconn import getconn

def delete_data():
    conn = getconn()
    cur = conn.cursor()
    # 103번 삭제
    sql = "delete from member where mem_num = 103 "
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_data()
