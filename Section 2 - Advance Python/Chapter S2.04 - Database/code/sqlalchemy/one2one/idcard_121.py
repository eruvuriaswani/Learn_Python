import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    card = Column(Integer, ForeignKey('card.id'))
    child = relationship("Card", backref=backref("user", uselist=False), uselist=False)


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    # parent_id = Column(Integer, ForeignKey('parent.id'))
    # parentage = relationship("Parent", backref=backref("child", uselist=False))


DB_FILE = "idcard.sqlite3"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)
engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

mycard = Card(number="007007", user=User(name="mayank"))

session.add(mycard)
session.flush()
session.commit()

session.close()
engine.dispose()
