import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import string, random

from apps import app, db


app.config.from_pyfile('config.py')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


# from flask import Flask
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)

# # app.config.from_object('config')
# app.config.from_pyfile('config.py')

# db = SQLAlchemy(app)
# import models
# migrate = Migrate(app, db)

# app.secret_key = 'development key'

# # basedir = os.path.abspath(os.path.dirname(__file__))

# # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')
# # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

# from apps import routes

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# login_manager.session_protection = "strong"

# cli_manager = Manager(app)
# cli_manager.add_command('db', MigrateCommand)


# if __name__ == '__main__':
#     cli_manager.run()
