from flask import Flask, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


# data = {'a': '北京', 'b': '上海', 'c': '武汉'}
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!!!'
#
#
# @app.route('/city/<key>')
# def get_city(key):
#     return data.get(key)
#
#
# @app.route('/add/<int:num>')
# def add(num):
#     result = num + 10
#     return str(result)
#
#
# @app.route('/index/<path:p>')
# def get_path(p):
#     return p
#
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/index')
# def index():
#     return {'a': '北京', 'b': '上海', 'c': '武汉'}  # application/json
#
#
# @app.route('/index1')
# def index1():
#     return '<h1>北京</h1>'  # Content-Type:text/htmL;charset=utf-8
#
#
# # return 后面返回的字符串其实也是做了一个response对象的封装。最终的返回结果还是response对象
#
# @app.route('/index2')
# def index2():
#     return 'sorry', 404
#
#
# @app.route('/index3')
# def index3():
#     return Response('<h1>大家想好中午吃什么了吗？</h1>')
#
#
# @app.route('/register')
# def register():
#     r = render_template('register.html')
#     return r
#
#
# @app.route('/register2', methods=['GET', 'POST'])
# def register2():
#     print(request.full_path)
#     print(request.path)
#     print(request.args)  # dict类型
#     # print(request.args.get('username'))  # get方式传参才能收到
#     # print(request.args.get('password'))
#
#     print(request.form)
#     print(request.form.get('username'))
#     print(request.form.get('password'))
#     return '进来了'

# @app.route('/')
# def hello_world():
#     msg = ' hello everyone hello world'
#     li = [3, 7, 9, 1, 5]
#     return render_template('define_filter.htmL', msg=msg, li=li)
#
#
# # 过滤器本质就是函数
# # 第一种方式
# def replace_hello(value):
#     print('------>', value)
#     value = value.replace(' hello ', '')
#     print('======>', value)
#     return value.strip()
#
#
# app.add_template_filter(replace_hello, 'replace')
#
#
# # 第二种方式 装饰器
# @app.template_filter('listreverse')
# def reverse_list(li):
#     temp_li = list(li)
#     temp_li.reverse()
#     return temp_li

@app.route('/base')
def load_base():
    return render_template('base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/macro')
def use_macro():
    return render_template('macro/macro1.html')


@app.route('/macro1')
def use_macro1():
    return render_template('macro/macro2.html')


if __name__ == '__main__':
    app.run()
