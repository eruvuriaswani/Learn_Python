from flask import Flask
from flask.ext.bower import Bower
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.auth import AuthModule
from app.common import Common
from app.admin.views import Admin


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.ConfigDev')

    db.init_app(app)

    Bower(app)

    AuthModule(app, db)
    Admin(app)
    Common(app)

    return app


def create_users():
    """ Create users when app starts """
    from app.auth.models import find_or_create_role, find_or_create_user

    db.create_all()
    # Adding roles
    admin_role = find_or_create_role('admin', u'Admin')
    # Add users
    find_or_create_user(u'admin', u'', u'admin@ikeasi.com',
                        'admin', admin_role)
    find_or_create_user(u'user', u'', u'user@ikeasi.com',
                        'user', None)

    # Save to DB
    db.session.commit()
