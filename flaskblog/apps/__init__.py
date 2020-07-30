from flask import Flask

from settings import DevelopmentConfig

from exts import db

from apps.user.views import user_bp

from apps.article.view import article_bp

from exts import bootstrap


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    # 初始化db
    db.init_app(app=app)
    bootstrap.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    return app
