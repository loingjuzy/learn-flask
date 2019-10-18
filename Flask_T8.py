from flask import Flask, url_for, views, jsonify

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
})


# 父类，把数据转换成json格式
class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


# 子类只需要写get_data方法
class ListView(JsonView):
    def get_data(self):
        return {"usernmae": 'derek', 'age': 18}


app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
