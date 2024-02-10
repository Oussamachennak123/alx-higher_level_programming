#!/usr/bin/python3
""" define fonction read_file(filename="")"""


def read_file(filename=""):
    with open('UTF8', 'r') as f:
        filename = f.read()
        print(filename, end="")
