#!/usr/bin/python3
""" create class BaseGeometry"""


class BaseGeometry:
    """ define class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value > 0:
            ValueError(f"{name} must be greater than 0")
