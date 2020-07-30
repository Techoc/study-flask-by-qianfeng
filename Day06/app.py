from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.models import User
from apps.article.models import *
from apps import create_app

from exts import db

app = create_app()

mananger = Manager(app=app)

# 配置命令行工具管理db
migrate = Migrate(app=app, db=db)
mananger.add_command('db', MigrateCommand)

if __name__ == '__main__':
    mananger.run()
