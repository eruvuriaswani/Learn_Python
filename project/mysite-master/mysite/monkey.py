# -*- coding: utf-8 -*-
import sys
from functools import wraps
from types import FunctionType
from flask import current_app
from flask.ext.login import login_required, current_user


# the decorator login_required from flask login
def permission_required(permission):
    def _permission_required(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if current_app.login_manager._login_disabled:
                return func(*args, **kwargs)
            elif not current_user.is_authenticated():
                return current_app.login_manager.unauthorized()
            elif not current_user.has_perm(permission):
                raise RuntimeError('Access is forbidden')
            return func(*args, **kwargs)

        return decorated_view

    return _permission_required


def _dispatch_required(x=None):
    if type(x) == FunctionType:
        return login_required(x)
    elif isinstance(x, basestring):
        return permission_required(x)
    elif x is None:
        return login_required
    else:
        raise ValueError('The argument is invalid')


def patch_login_required():
    sys.modules['flask.ext.login'].login_required = _dispatch_required


def patch_all():
    patch_login_required()
