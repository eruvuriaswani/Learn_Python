from flask import Blueprint
from . import views


class Common(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        common = Blueprint('common', __name__)

        common.add_url_rule('/', 'index', views.index)
        app.register_blueprint(common)
