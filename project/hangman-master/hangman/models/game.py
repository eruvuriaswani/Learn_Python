from datetime import datetime
from hangman.models import db


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.String(50)) # System will have pre-generated categories
    answer = db.Column(db.String(100))  # Extreme length for really difficult games
    guesses = db.Column(db.Text)        # En/Decoded as json for array representation
    misses = db.Column(db.Text)         # En/Decoded as json for array representation
    board = db.Column(db.Text)          # En/Decoded as json for array representation
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    loser_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, category, answer):
        self.category = category
        self.answer = answer
        self.start_date = datetime.utcnow()
        self.guesses = ''
        self.misses = ''
        self.board = ''

    def __repr__(self):
        return '<Game %s: %s>' % (self.id, self.category)
