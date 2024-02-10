#!/usr/bin/python3
""" define fonction write a text with fonction write_file"""
def write_file(file="", text=""):
    with open(file, 'w', encoding="utf-8") as f:
        return f.write(text)
