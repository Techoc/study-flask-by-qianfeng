from flask import Blueprint, request, render_template, redirect
import flask

from apps.User.model import User

user_bp = Blueprint('user', __name__)

# 列表保存的是一个一个的用户对象
users = []


@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')

        if password == repassword:
            # 用户名唯——
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')
            # 创建User对象
            user = User(username, password, phone)
            # 添加到用户列表
            users.append(user)
            return redirect('/')
    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登录'


@user_bp.route('/del')
def del_user():
    # 获取传递的username
    username = request.args.get('username')
    # 根据username找到列表中的user对象
    for user in users:
        if user.username == username:
            # 删除user
            users.remove(user)
            return redirect('/')
    else:
        return '删除失败'


@user_bp.route('/update', methods=['POST', 'GET'], endpoint='update')
def update_user():
    if request.method == 'POST':
        realname = request.form.get('realname')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == realname:
                user.username = username
                user.phone = phone
                return '更改成功！'
    else:
        # get请求了
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                return render_template('user/update.html', user=user)


@user_bp.route('/loginout', methods=['GET', 'POST'])
def loginout():
    return '用户退出'
