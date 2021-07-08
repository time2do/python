from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    # sql - select
    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall()  # 데이터 목록 리스트 반환
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = sql = "select * from employee where emp_id = ? "
    cur.execute(sql, ('e103',))  # 튜플이라 하나 일때는 뒤에 콤마 찍어야 함
    rs = cur.fetchone()
    print(rs)
    conn.close()

def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?,?,?,?)"
    cur.execute(sql, ('e104', '김산', 22, 5000))
    conn.commit()
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    # 박인비 salary 를 25000으로 바꾸기
    sql = "update employee set salary = ? where emp_id = ?"
    cur.execute(sql, (25000, 'e102'))
    conn.commit()
    conn.close()

def delete_emp():
    conn = getconn()
    cur = conn.cursor()
    # 사원번호 e102 지우기
    sql = "delete from employee where emp_id = ? "
    cur.execute(sql, ('e102',))
    conn.commit()
    conn.close()


if __name__=="__main__":
    # insert_emp()
    #update_emp() #  업데이트가 select 위에 있어야 변경후 보여줌
    delete_emp()
    select_emp()
    # select_one()
