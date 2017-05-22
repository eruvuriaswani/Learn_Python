from flask import render_template
from flask_user import roles_required
from . import admin_bp


class Admin(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(admin_bp, url_prefix="/admin")


@admin_bp.route('/')
@roles_required('admin')
def index():
    return render_template('admin/index.html')
