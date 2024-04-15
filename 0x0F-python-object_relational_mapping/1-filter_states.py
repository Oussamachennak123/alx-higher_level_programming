#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    mysql__username = sys.argv[1]
    mysql__password = sys.argv[2]
    db__name = sys.argv[3]

    try:  # si mysql est connecté
        connected = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql__username,
            passwd=mysql__password,
            db=db__name,
            charset="utf8"
        )
    except MySQLdb.Error as e:  # sinon affiche ce msg
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    curl = connected.cursor()
    curl.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = curl.fetchall()

    for row in rows:
        print(row)

    curl.close()
    connected.close()
