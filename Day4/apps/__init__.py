from flask import Flask

import settings
from apps.User.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # app是核心对象
    app.config.from_object(settings)  # 加载配置
    # 蓝图
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
