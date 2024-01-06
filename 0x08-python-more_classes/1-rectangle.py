#!/usr/bin/python3

""" define class Rectangle"""


class Rectangle:
    """ creation class Rectangle """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property  # propert width
    def width(self):
        return self.__width

    @width.setter  # setter width with value
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property  # create property heighit
    def height(self):
        return self.__height

    @height.setter  # setter height with value
    def height(self, value):
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
