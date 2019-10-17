from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'abcdef'


@app.before_request
def process_request1(*args, **kwargs):
    print('request1进来')


@app.before_request
def process_request2(*args, **kwargs):
    print('request2进来')


@app.after_request
def process_response1(response):
    print('response1走了')
    return response


@app.after_request
def process_response2(response):
    print('response2走了')
    return response


@app.route('/index', methods=['GET'])
def index():
    print('index函数')
    return 'hello'


@app.errorhandler(404)
def error_404(arg):
    return '404错误'


if __name__ == '__main__':
    app.run()
