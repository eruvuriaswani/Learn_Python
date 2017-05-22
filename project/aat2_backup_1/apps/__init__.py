from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

app.secret_key = 'development key'

# basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from apps import routes
