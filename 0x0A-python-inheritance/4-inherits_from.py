#!/usr/bin/python3
""" define def inherits_from"""


def inherits_from(obj, a_class):
    """  that prints the list, but sorted (ascending sort) """
    if isinstance(obj, a_class) and issubclass(type(obj), a_class):
        return True
    return False
