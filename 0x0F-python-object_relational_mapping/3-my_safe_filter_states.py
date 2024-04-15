#!/usr/bin/python3
"""
Script takes in an argument and displays all values in the states
where `name` matches the argumentfrom the database `hbtn_0e_0_usa`
This time the script is safe from MySQL injections
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db_connected = db.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])

    db_cursorl = db_connected.cursor()
    db_cursorl.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursorl.fetchall()

    for row in rows_selected:
        print(row)
