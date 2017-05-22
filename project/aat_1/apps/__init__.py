# from flask_sqlalchemy import create_engine, ForeignKey
# from flask_sqlalchemy import Column, Integer, String, Boolean
# from flask_sqlalchemy.orm import sessionmaker, relationship, backref

# db = SQLAlchemy(db=SQLAlchemy(app))

from flask import Flask, render_template
app = Flask(__name__)
app.debug = True   # Not for production

@app.route('/')
def hello():
    return render_template('index.html')