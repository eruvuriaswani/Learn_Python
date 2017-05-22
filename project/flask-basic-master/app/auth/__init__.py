from flask_user import UserManager, SQLAlchemyAdapter
from .models import User, MyRegisterForm


class AuthModule(object):
    def __init__(self, app=None, db=None):
        if app is not None:
            self.init_app(app, db)

    def init_app(self, app, db):
        db_adapter = SQLAlchemyAdapter(db, User)
        UserManager(db_adapter, app, register_form=MyRegisterForm)
