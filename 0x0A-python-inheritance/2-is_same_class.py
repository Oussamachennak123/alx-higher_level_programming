#!/usr/bin/python3
""" define fontion is_same_class"""


def is_same_class(obj, a_class):
    """ Check if an object is exactly an instance of a given class """
    if type(obj) == a_class:
        return True
    return False
