#!/usr/bin/python3
""" define fonction read_file(filename="")"""


def read_file(file=""):
    with open(file, encoding="UTF8") as f:
        print(f.read(), end="")
