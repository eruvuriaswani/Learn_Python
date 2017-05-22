from wtforms.validators import data_required

from hangman.models import Game
from . import BaseAdminModelView


class AdminGameView(BaseAdminModelView):
    can_view_details = True

    form_args = {
        'category': {
            'validators': [data_required()]
        },
        'answer': {
            'validators': [data_required()]
        },
        'host': {
            'validators': [data_required()]
        }
    }

    def __init__(self, session, **kwargs):
        super(AdminGameView, self).__init__(Game, session, **kwargs)
