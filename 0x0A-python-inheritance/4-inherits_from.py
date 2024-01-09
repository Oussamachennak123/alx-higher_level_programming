#!/usr/bin/python3
""" define def inherits_from"""


def inherits_from(obj, a_class):
    """  that prints the list, but sorted (ascending sort) """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
