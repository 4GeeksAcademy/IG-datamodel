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
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    lastName = Column(String(60), nullable=False)
    birthDate = Column(String(10), nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    identity = Column(String(20), nullable=False)
    publication_id =  Column(Integer, ForeignKey('Publications.id'))
    story = Column(Integer, ForeignKey('Storys.id'))
    other_accounts = Column(Integer, ForeignKey('Other_accounts.id'))


class Other_Acounts(Base):
    __tablename__ = 'other_acounts'
    id = Column(Integer, primary_key=True)
    twitter = Column(String)
    whastapp = Column(Integer)
    facebook = Column(String(50))
    misc = Column(String(50))

class Commentarys(Base): 
    __tablename__ = 'commentarys'
    id = Column(Integer, primary_key=True, ForeignKey='User.id')
    text = Column(String(250))


class Publications(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    src = Column(String, nullable=False)
    description = Column(String)

class Storys(Base):
    __tablename__ = 'storys'
    id = Column(Integer,primary_key=True)
    src = Column(String(100))

class Notifications(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True, ForeignKey='User.id')
    id_origin = Column(Integer)
    id_destination = Column(Integer)
    type = Column(String)

class NotificationType(Base):
    __tablename__ = 'notification_type'
    like = Column(bool, ForeignKey='Notifications.type')
    new_follower = Column(int, ForeignKey='Notifications.type')
    mention = Column(Integer, ForeignKey='Notifications.type')
    collaborator = Column(Integer, ForeignKey='Notifications.type')
                  

class Followers(Base):
    __tablename__ = 'followers'
    
    user_from_id = Column(bool, ForeignKey='User.id')
    user_to_id = Column(bool, ForeignKey='User.id')






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
