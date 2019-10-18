from flask import Flask, request, url_for

# 创建一个Flask对象，传递__name__参数进去
app = Flask(__name__)
app.config.from_pyfile('config.py')


# url与视图映射
@app.route('/')
def hello_world():
    return url_for('my_list',page=2,count=2)


@app.route('/list/<page>/')
def my_list(page):
    return 'my_list'


@app.route('/<any(blog,user):url_path>/<id>')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情%s' % id
    else:
        return '用户详情%s' % id


@app.route('/article/<path:test>/')
def test_article(test):
    return 'test_article:{}'.format(test)


@app.route('/tieba/')
def tieba():
    wd = request.args.get('wd')
    print(request.args['wd'])
    return '获取的参数的是%s' % wd


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)  # flask中的一个测试应用服务器
