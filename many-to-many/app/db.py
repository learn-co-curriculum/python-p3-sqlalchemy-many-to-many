import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import (create_engine,
    Column, Integer, String, ForeignKey)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')

Base = declarative_base()
