#!/usr/bin/python3
"""Define class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):  # user class BaseGemetry
    """ define Rectangle using BaseGeometry"""
    def __init__(self, width, height):
        """ new rectangle user"""
        self.integer_validator = ("width", width)
        self.__width = width
        self.integer_validator = ("height", height)
        self.__height = height

    def __area__(self):
        return self.__height * self.__width
