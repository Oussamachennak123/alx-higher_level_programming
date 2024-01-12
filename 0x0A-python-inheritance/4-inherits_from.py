#!/usr/bin/python3
"""
    Check if an object inherits from a specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check for inheritance.

    Returns:
    True if the object inherits from the specified class, False otherwise.
"""


def inherits_from(obj, a_class):
    """  that prints the list, but sorted (ascending sort) """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
