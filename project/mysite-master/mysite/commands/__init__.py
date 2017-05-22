from flask.ext.script import Manager, prompt_bool
from ..models import db

manager = Manager()
manager.add_default_commands()

@manager.command
def create_all_tables():
    if prompt_bool(
        'Are you sure you want to create all tables?',
        default=True):
        db.create_all()

@manager.command
def drop_all_tables():
    if prompt_bool(
        'Are you sure you want to drop all tables?',
        default=False):
        db.drop_all()

@manager.command
def recreate_all_tables():
    if prompt_bool(
        'Are you sure you want to recreate all tables?',
        default=False):
        db.drop_all()
        db.create_all()
