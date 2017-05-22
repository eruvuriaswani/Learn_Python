from flask_security import UserMixin

from hangman.models import db, roles_users


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )

    hosted_games = db.relationship('Game',
                                   primaryjoin='and_(User.id==Game.host_id)',
                                   backref='host',
                                   lazy='dynamic')
    games_played = db.relationship('Game',
                                   primaryjoin='and_(User.id==Game.player_id)',
                                   backref='player',
                                   lazy='dynamic')
    games_won = db.relationship('Game',
                                primaryjoin='and_(User.id==Game.winner_id)',
                                backref='winner',
                                lazy='dynamic')
    games_lost = db.relationship('Game',
                                 primaryjoin='and_(User.id==Game.loser_id)',
                                 backref='loser',
                                 lazy='dynamic')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return 'User: %s' % self.username
