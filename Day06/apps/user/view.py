import hashlib

from flask import Blueprint, render_template, request, redirect, url_for

from apps.user.models import User

from exts import db
from sqlalchemy import or_

user_bp = Blueprint('user', __name__)


# 用户注册
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8 ')).hexdigest()
            user.phone = phone
            # 添加并提交用户
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.user_center'))
    return render_template('user/register.html')


# 用户中心
@user_bp.route('/')
def user_center():
    # 查询数据库中的数据
    users = User.query.filter(User.isdelete == False).all()  # select * from user;
    return render_template('user/center.html', users=users)


# 登录
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 关键 select * from user where username='xxx'
        new_password = hashlib.sha256(password.encode('utf-8 ')).hexdigest()
        user_list = User.query.filter_by(username=username)
        for u in user_list:
            # 此时的u表示的就是用户对象
            if u.password == new_password:
                return '用户登录成功！'
        else:
            return render_template('user/login.html', msg='用户名或密码有误！')
    return render_template('user/login.html')


# 搜索
@user_bp.route('/search')
def search():
    keyword = request.args.get('search')
    # 查询数据库
    user_list = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user/center.html', users=user_list)


# 用户删除
@user_bp.route('/delete', endpoint='delete')
def user_delete():
    # 获取用户id
    id = request.args.get('id')
    # 1. 逻辑删除
    # 获取该id的用户
    user = User.query.get(id)
    # 逻辑删除：
    user.isdelete = True
    # 提交
    db.session.commit()

    # 2. 物理删除
    # user = User.query.get(id)
    # db.session.delete(user)
    # db.session.commit()
    return redirect(url_for('user.user_center'))


# 用户信息更新
@user_bp.route('/update', endpoint='update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')
        # 找用户
        user = User.query.get(id)
        # 改用户信息
        user.username = username
        user.phone = phone
        # 提交
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)
