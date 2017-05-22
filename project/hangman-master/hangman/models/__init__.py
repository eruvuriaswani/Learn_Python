from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_security import Security as _Security


db = _SQLAlchemy()
security = _Security()


from .game import Game
from .role import Role
from .tables import roles_users
from .user import User


def _populate__all__(lcls):
    global __all__
    import inspect as _inspect

    __all__ = sorted(name for name, obj in lcls.items()
                     if not (name.startswith('_') or _inspect.ismodule(obj)))


_populate__all__(locals())
