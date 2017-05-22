#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from app import create_app, create_users


app = create_app()
manager = Manager(app)


@manager.command
def init_db():
    create_users()


if __name__ == "__main__":
    manager.run()
