from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.debug = True
app.secret_key = 'abcdef'

USERS = {
    1: {'name': 'derek', 'age': 18},
    2: {'name': 'tom', 'age': 20},
    3: {'name': 'jack', 'age': 22},
}


@app.route('/detail/<int:nid>', methods=['GET'])
def detail(nid):
    # 没登录不能访问
    user = session.get('user_info')
    if not user:
        return redirect('/login')
    info = USERS.get(nid)
    return render_template('detail.html', info=info)


@app.route('/index', methods=['GET'])
def index():
    # 没登录不能访问
    user = session.get('user_info')
    if not user:
        # return redirect('/login')
        # 根据设置的别名反向生成url
        url = url_for('login11')
        return redirect(url)
    return render_template('index.html', user_dict=USERS)


@app.route('/login', methods=['GET', 'POST'], endpoint='login11')  # endpoint起别名
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'derek' and pwd == '123':
            # 添加session值
            user = session['user_info'] = user
            return redirect('/index')
        return render_template('login.html', error='用户名或密码错误')


if __name__ == '__main__':
    app.run()
