# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask, render_template, url_for
from flask.ext.login import LoginManager
from . import constants
from . import monkey

monkey.patch_all()


def create_app(name=None, settings=None):
    """http://flask.pocoo.org/docs/patterns/appfactories/"""
    app = Flask(name or __name__)

    with app.app_context():
        # register settings
        # priority: params > settings.py > env variable
        app.config.from_envvar('TESTBOX_SETTINGS', silent=True)
        app.config.from_pyfile('settings.py')
        if settings is not None:
            if isinstance(object, settings):
                app.config.from_object(settings)
            elif os.path.isfile(os.path.join(app.root_path, settings)):
                app.config.from_pyfile(settings)

        logging.debug('Add global templates function')
        app.jinja_env.globals['static'] = (lambda filename: url_for('static', filename=filename))
        app.jinja_env.globals['constants'] = constants
        app.jinja_env.add_extension('jinja2.ext.do')

        logging.debug('Register error process handlers')
        @app.errorhandler(404)
        def http404(error):
            return render_template('404.html'), 404

        @app.errorhandler(500)
        def http500(error):
            return render_template('500.html'), 500

        logging.debug('Add user login manager')
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = 'auth.login'

        @login_manager.user_loader
        def user_loader(user_id):
            from .models import User
            return User.query.get(user_id)

        logging.debug('Initialize the database')
        from .models import db
        db.init_app(app)

        logging.debug('Register blueprints')
        from .views.main import main
        app.register_blueprint(main)
        from .views.auth import auth
        app.register_blueprint(auth, url_prefix='/auth')
        return app
