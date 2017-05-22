from flask import redirect, url_for, request, abort
from flask_admin.contrib.sqla import ModelView as _ModelView
from flask_wtf import Form as _WTForm
from flask_security import login_required as _login_required, current_user as _current_user


class BaseAdminModelView(_ModelView):
    form_base_class = _WTForm

    def is_accessible(self):
        if _current_user.is_active() and \
           _current_user.is_authenticated() and \
           _current_user.has_role('superuser'):
            return True

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible
        :param name:
        :param kwargs:
        :return:
        """
        if not self.is_accessible():
            if _current_user.is_authenticated():
                abort(403)
            else:
                return redirect(url_for('security.login', next=request.url))


from .game_view import AdminGameView
from .user_view import AdminUserView


def _populate__all__(lcls):
    global __all__
    import inspect as _inspect

    __all__ = sorted(name for name, obj in lcls.items()
                     if not (name.startswith('_') or _inspect.ismodule(obj)))


_populate__all__(locals())
