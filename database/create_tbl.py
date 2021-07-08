# member db 에 member 테이블 생성
# db 프로세스
# 1. db에 연결
# 2. 테이블 생성

from libs.db.dbconn import getconn

def create_table():
    conn = getconn() # dbconn 모듈에서 getconn 호출 ( 객체 생성 )
    cur = conn.cursor() # db 작업을 하는 객체(cur)
    # 테이블 생성 - sql 언어 DDL
    # primary key 중복불가 키 생성- 여기서는 번호 중복 불가
    sql = """
        create table member(
            mem_num int primary key, 
            name char(20),
            age int
        )
    """
    cur.execute(sql)

    conn.commit()  # 트랜잭션 완료(수행)
    conn.close()  # 네트워크 종료

if __name__ == "__main__":
    create_table()
