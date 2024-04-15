#!/usr/bin/python3
import MySQLdb
from sys import argv

""" script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    commandDB_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, password=argv[2], db=argv[3]
    )

    cursor_DB = commandDB_connect.cursor()  # cursor_DB objet de curseur

    cursor_DB.execute("SELECT * FROM states")

    all_selected = cursor_DB.fetchall()  # affiche tous les lignes

    for a in all_selected:  # imprimer les résultats de la requête SELECT
        print(a)
