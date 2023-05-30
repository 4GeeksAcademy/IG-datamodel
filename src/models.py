import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(20), nullable=False)
    lastName = Column(String(60), nullable=False)
    birthDate = Column(String(10), nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False)
    whatsapp = Column(String(50))
    facebook = Column(String(50))
    twitter = Column(String(50))


class Commentarys(Base): 
    __tablename__ = 'commentarys'
    id = Column(Integer, primary_key=True)
    user_comment = Column(String(250), ForeignKey('user.id'))
    publication = Column(String(250), ForeignKey('publications.id')) 
    text = Column(String(250))


class Publications(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    src = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

class Storys(Base):
    __tablename__ = 'storys'
    id = Column(Integer,primary_key=True)
    src = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Notifications(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    user_notification = Column(String(250), ForeignKey('user.id'))
    id_origin = Column(Integer, unique=True)
    id_destination = Column(Integer, unique=True)
    type = Column(String(250), nullable=False)


class Followers(Base):
    __tablename__ = 'followers'
    folloers_id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
