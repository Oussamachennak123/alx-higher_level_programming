#!/usr/bin/python3

"""
This script prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db__url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db__url)
    Session = sessionmaker(bind=engine)

    sessionn = Session()

    results = sessionn.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    sessionn.commit()
    sessionn.close()
