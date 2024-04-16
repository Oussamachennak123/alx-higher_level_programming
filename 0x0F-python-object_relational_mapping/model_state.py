#!/usr/bin/python3

"""
Script defines a State class and
a Base class to work with MySQLAlchemy ORM
"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """define State class
    Attributes:
        __tablename__ (str): The table name of class
        id (int): The State id of class
        name (str): The State name of class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary__key=True)
    name = Column(String(128), nullable=False)
