from flask import Flask, render_template

app = Flask(__name__)  #이렇게 쓰는건 약속임

@app.route('/') #루트 경로 http://127.0.0.1:5000
def index():
    return render_template("index.html")

@app.route('/register')  # 새로운 페이지 생성, http://127.0.0.1:5000/register
def register():
    return "<h1>회원가입 페이지입니다</h1>"

@app.route('/board')
def board():
    return "<h1>게시판 목록입니다</h1>"

if __name__=="__main__":
    app.run()  #실행