from wtforms.validators import data_required

from hangman.models import User
from . import BaseAdminModelView


class AdminUserView(BaseAdminModelView):
    can_view_details = True
    column_searchable_list = ['username', ]
    # column_filters = ['username', ]

    form_args = {
        'username': {
            'label': 'Username',
            'validators': [data_required()]
        }
    }

    def __init__(self, session, **kwargs):
        super(AdminUserView, self).__init__(User, session, **kwargs)
