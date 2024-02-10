#!/usr/bin/python3
""" define fonction read_file(filename="")"""


def read_file(file=""):
    """ read the text with UTF8"""
    with open(file, encoding="utf-8") as f:
        print(f.read(), end="")
