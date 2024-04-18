#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """

    db_urll = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_urll)
    Session = sessionmaker(bind=engine)

    sessionn = Session()

    states = sessionn.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            sessionn.delete(state)

    sessionn.commit()

    sessionn.close()
