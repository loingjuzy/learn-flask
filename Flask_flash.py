from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.debug = True
app.secret_key = 'abcdef'


@app.route('/get')
def get():
    data = get_flashed_messages()
    print(data)
    return 'hello world'


@app.route('/set')
def set():
    # 向某个地方设置一个值
    flash('访问一次就设置一次')
    return 'hello world'


if __name__ == '__main__':
    app.run()
