#!/usr/bin/python3
"""
A custom list class that inherits from
the built-in list class
"""


class MyList(list):
    """ define class MyList that inherits from list """
    def print_sorted(self):
        """ define fontion print_sorted """
        print(sorted(self))
