# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def create_session(path, echo=False):
    engine = create_engine('sqlite:///' + path, echo=echo)

    return sessionmaker(bind=engine)
