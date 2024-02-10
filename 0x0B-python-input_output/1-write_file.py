#!/usr/bin/python3
""" define fonction write a text with fonction write_file"""


def write_file(filename="", text=""):
    """ fonction for user write a text"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
