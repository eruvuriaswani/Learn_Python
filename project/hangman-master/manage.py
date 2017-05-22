from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from hangman.app import create_app, create_db
from hangman.models import *


app = create_app()
db = SQLAlchemy(app)
security = Security(app)
