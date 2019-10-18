from flask import Flask, url_for, Response, jsonify

app = Flask(__name__)
app.config.from_pyfile('config.py')


class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """这个方法只有视图函数返回非字符、非元祖、非Response对象才会调用
        :param response:
        :param environ:
        :return:
        """
        # 把字典转换成json
        if isinstance(response, dict):
            # jsonify将字典转换成json对象，还将该对象包装成了一个Response对象
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)


app.response_class = JsonResponse


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/list1/')
def list1():
    return Response('list1')  # 合法对象，直接返回


@app.route('/list3/')
def list3():
    return {'username': 'derek', 'age': 18}  # 返回的是非字符、非元祖、非Response对象，所以执行force_type方法


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
