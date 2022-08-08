import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, ForeignKeyConstraint, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')

Base = declarative_base()

class GameUser(Base):
    __tablename__ = "game_users"

    game_id = Column(ForeignKey('games.id'), primary_key=True)
    user_id = Column(ForeignKey('users.id'), primary_key=True)

    game = relationship('Game',
        backref=backref('users'))
    user = relationship('User',
        backref=backref('games'))

    def __repr__(self):
        return f'GameUser(game_id={self.game_id}, ' + \
            f'user_id={self.user_id})'

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', backref=backref('game'))

    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)

    score = Column(Integer())
    comment = Column(String())

    game_id = Column(Integer(), ForeignKey('games.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id}, ' + \
            f'user_id={self.user_id})'

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    reviews = relationship('Review', backref=backref('user'))

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'name={self.name})'
