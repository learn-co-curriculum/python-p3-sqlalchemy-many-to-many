from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conftest import SQLITE_URL
from models import User, Game, Review

class TestReview:
    '''Review in models.py'''

    def test_has_attributes(self):
        '''has attributes id, score, comment, game_id, and user_id.'''
        
        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        review = Review(score=2, comment="Very bad!")
        session.add(review)
        session.commit()

        assert hasattr(review, "id")
        assert hasattr(review, "score")
        assert hasattr(review, "comment")
        assert hasattr(review, "game_id")
        assert hasattr(review, "user_id")

        session.query(Review).delete()
        session.commit()

    def test_has_one_user_id(self):
        '''has an attribute "user_id", an int that is a foreign key to the users table.'''

        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        user = User(name="Ben")
        session.add(user)
        session.commit()

        review = Review(score=4, comment="Fairly bad!")
        review.user_id = user.id
        session.add(review)
        session.commit()

        assert type(review.user_id) == int
        assert review.user_id == user.id

        session.query(User).delete()
        session.query(Review).delete()
        session.commit()

    def test_has_one_user(self):
        '''has an attribute "user" in the ORM that is a record from the users table.'''

        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        user = User(name="Ben")
        session.add(user)
        session.commit()

        review = Review(score=4, comment="Fairly bad!")
        review.user = user
        session.add(review)
        session.commit()

        assert review.user
        assert review.user_id == user.id
        assert review.user == user

        session.query(User).delete()
        session.query(Review).delete()
        session.commit()

    def test_has_one_game_id(self):
        '''has an attribute "game_id", an int that is a foreign key to the games table.'''

        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        game = Game(title="Javelinna")
        session.add(game)
        session.commit()

        review = Review(score=9, comment="Iconic.")
        review.game_id = game.id
        session.add(review)
        session.commit()

        assert type(review.game_id) == int
        assert review.game_id == game.id

        session.query(Game).delete()
        session.query(Review).delete()
        session.commit()

    def test_has_one_game(self):
        '''has an attribute "game" in the ORM that is a record from the games table.'''

        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        game = Game(title="Shady Spirits")
        session.add(game)
        session.commit()

        review = Review(score=10, comment="GGOAT")
        review.game = game
        session.add(review)
        session.commit()

        assert review.game
        assert review.game_id == game.id
        assert review.game == game

        session.query(Game).delete()
        session.query(Review).delete()
        session.commit()
