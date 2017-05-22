def create_db(app):
    """
    Initialize the database with our models
    :return: None
    """
    import hangman.models
    hangman.models.db.create_all(app=app)
    return hangman.models.db


def create_app(config='dev'):
    """
    Create our application and initialize the database.
    :param config: The type of default configuration to load.  [dev, prod]
    :return: An initialized Flask() object
    """
    from flask import Flask as _Flask
    from .configuration import DevConfiguration
    app = _Flask(__name__)
    if config == 'dev':
        app.config.from_object(DevConfiguration)

    # Initialize the DB object with our app
    from hangman.models import db, User, Game, Role, roles_users
    db.init_app(app)

    # Configure flask_admin views
    from flask_admin import Admin, helpers as admin_helpers
    from hangman.views.admin import AdminGameView, AdminUserView
    admin = Admin(app, 'Hangman Admin', template_mode='bootstrap3')
    admin.add_view(AdminUserView(db.session))
    admin.add_view(AdminGameView(db.session))

    # Initialize security
    from flask_security import Security, SQLAlchemyUserDatastore
    from hangman.models import security
    # security = Security(app, SQLAlchemyUserDatastore(db, User, Role))

    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
        )

    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role))


    return app


def _populate__all__(lcls):
    global __all__
    import inspect as _inspect

    __all__ = sorted(name for name, obj in lcls.items()
                     if not (name.startswith('_') or _inspect.ismodule(obj)))


_populate__all__(locals())
