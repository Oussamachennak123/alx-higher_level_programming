#!/usr/bin/python3
""" define fonction add the new line a text"""


def append_write(filename="", text=""):
    """ user a for add in the text"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
