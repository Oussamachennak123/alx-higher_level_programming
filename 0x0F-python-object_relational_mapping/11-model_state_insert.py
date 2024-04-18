#!/usr/bin/python3

"""
This script adds the State object
`Louisiana` to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database
    """

    db_urll = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_urll)
    Session = sessionmaker(bind=engine)

    session = Session()

    new__state = State(name="Louisiana")
    session.add(new__state)
    session.commit()

    print('{0}'.format(new__state.id))
    session.close()
