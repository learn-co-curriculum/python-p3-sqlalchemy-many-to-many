from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# Table object
# PASSING

# game_user = Table(
#     'game_users',
#     Base.metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('game_id', ForeignKey('games.id')),
#     Column('user_id', ForeignKey('users.id')),
#     extend_existing=True,
# )

# class Game(Base):
#     __tablename__ = 'games'

#     id = Column(Integer(), primary_key=True)
#     title = Column(String())
#     genre = Column(String())
#     platform = Column(String())
#     price = Column(Integer())
#     created_at = Column(DateTime(), server_default=func.now())
#     updated_at = Column(DateTime(), onupdate=func.now())

#     users = relationship('User', secondary=game_user, back_populates='games')
#     reviews = relationship('Review', backref=backref('game'))

#     def __repr__(self):

#         return f'Game(id={self.id}, ' + \
#             f'title={self.title}, ' + \
#             f'platform={self.platform})'

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     created_at = Column(DateTime(), server_default=func.now())
#     updated_at = Column(DateTime(), onupdate=func.now())

#     games = relationship('Game', secondary=game_user, back_populates='users')
#     reviews = relationship('Review', backref=backref('user'))

#     def __repr__(self):

#         return f'User(id={self.id}, ' + \
#             f'name={self.name})'

# class Review(Base):
#     __tablename__ = 'reviews'

#     id = Column(Integer(), primary_key=True)

#     score = Column(Integer())
#     comment = Column(String())
#     created_at = Column(DateTime(), server_default=func.now())
#     updated_at = Column(DateTime(), onupdate=func.now())

#     game_id = Column(Integer(), ForeignKey('games.id'))
#     user_id = Column(Integer(), ForeignKey('users.id'))


#     def __repr__(self):

#         return f'Review(id={self.id}, ' + \
#             f'score={self.score}, ' + \
#             f'game_id={self.game_id})'

#######################################

# Association object
# PASSING

# class Game(Base):
#     __tablename__ = 'games'

#     id = Column(Integer(), primary_key=True)
#     title = Column(String())
#     genre = Column(String())
#     platform = Column(String())
#     price = Column(Integer())
#     created_at = Column(DateTime(), server_default=func.now())
#     updated_at = Column(DateTime(), onupdate=func.now())

#     reviews = relationship('Review', backref=backref('game'))
#     game_users = relationship('GameUser', back_populates='game')
#     users = association_proxy('game_users', 'user',
#         creator=lambda us: GameUser(user=us))

#     def __repr__(self):

#         return f'Game(id={self.id}, ' + \
#             f'title={self.title}, ' + \
#             f'platform={self.platform})'

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     created_at = Column(DateTime(), server_default=func.now())
#     updated_at = Column(DateTime(), onupdate=func.now())

#     reviews = relationship('Review', backref=backref('user'))
#     game_users = relationship('GameUser', back_populates='user')
#     games = association_proxy('game_users', 'game',
#         creator=lambda gm: GameUser(game=gm))

#     def __repr__(self):

#         return f'User(id={self.id}, ' + \
#             f'name={self.name})'

# class Review(Base):
#     __tablename__ = 'reviews'

#     id = Column(Integer(), primary_key=True)

#     score = Column(Integer())
#     comment = Column(String())
#     created_at = Column(DateTime(), server_default=func.now())
#     updated_at = Column(DateTime(), onupdate=func.now())

#     game_id = Column(Integer(), ForeignKey('games.id'))
#     user_id = Column(Integer(), ForeignKey('users.id'))

#     def __repr__(self):

#         return f'Review(id={self.id}, ' + \
#             f'score={self.score}, ' + \
#             f'game_id={self.game_id})'

# class GameUser(Base):
#     __tablename__ = "game_users"

#     id = Column(Integer(), primary_key=True)
#     game_id = Column(ForeignKey('games.id'))
#     user_id = Column(ForeignKey('users.id'))

#     game = relationship('Game', back_populates='game_users')
#     user = relationship('User', back_populates='game_users')

#     def __init__(self, game=None, user=None):
#         self.game = game
#         self.user = user

#     def __repr__(self):

#         return f'GameUser(game_id={self.game_id}, ' + \
#             f'user_id={self.user_id})'

#######################################

# Association object model
# PASSING

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    reviews = relationship('Review', back_populates='game')
    users = association_proxy('reviews', 'user',
        creator=lambda us: Review(user=us))

    def __repr__(self):

        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    reviews = relationship('Review', back_populates='user')
    games = association_proxy('reviews', 'game',
        creator=lambda gm: Review(game=gm))

    def __repr__(self):

        return f'User(id={self.id}, ' + \
            f'name={self.name})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)

    score = Column(Integer())
    comment = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    game_id = Column(Integer(), ForeignKey('games.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    game = relationship('Game', back_populates='reviews')
    user = relationship('User', back_populates='reviews')

    def __repr__(self):

        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'
