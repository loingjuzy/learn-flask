from flask import Flask, Response, jsonify
from Flask_PoolMysql import func

# 实例化flask对象
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


# 将'/'和函数index的对应关系加到路由中
@app.route('/')
def index():
    result_a = func('select * from book')
    result_b = func('select subgroup,count(*) from book group by subgroup')
    return {'first': result_a, 'twice': result_b}


@app.route('/get')
def get():
    result = func('select s.questionid,s.level,content,answer from question r join (select questionid,level from study order by RAND() limit 15) s on r.questionid = s.questionid')
    return {'topic': result}


if __name__ == '__main__':
    # 监听用户请求
    # 如果有用户请求到来，则执行app的__call__方法，app.__call__
    app.run()
