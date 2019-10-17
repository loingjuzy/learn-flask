from flask import Flask, render_template, Markup

app = Flask(__name__)
app.debug = True
app.secret_key = 'abcdef'


def func1(arg):
    return Markup(f"<input type='text' value='{arg}' />")


@app.route('/')
def index():
    return render_template('index-1.html', func1=func1)


if __name__ == '__main__':
    app.run()
