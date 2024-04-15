#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted in ascending
order by states.id
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql__username = sys.argv[1]
    mysql__password = sys.argv[2]
    db__name = sys.argv[3]

    try:
        connected = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql__username,
            passwd=mysql__password,
            db=db__name,
            charset="utf8"
        )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    curl = connected.cursor()
    curl.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curl.fetchall()

    for row in rows:
        print(row)

    curl.close()
    connected.close()
