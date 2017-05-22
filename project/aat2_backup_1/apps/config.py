import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
