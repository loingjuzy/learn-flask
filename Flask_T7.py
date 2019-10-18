from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


@app.route('/', endpoint='index')
def hello_world():
    print(url_for("derek_list"))  # 通过endpoint找到对应的url   /list/
    return render_template('index-2.html')


def my_list():
    return "列表页"


# 三个参数
# 1.url
# 2.给url起个别名，如果没有指定endpoint，则默认使用视图函数的名字作为endpoint的值
# 3.视图函数
app.add_url_rule('/list/', endpoint='derek_list', view_func=my_list)

with app.test_request_context():
    print(url_for('index'))  # /

if __name__ == '__main__':
    app.run()
