#!/usr/bin/python3

""" define class Rectangle"""


class Rectangle:
    """ creation class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property  # propert width
    def width(self):
        return self.__width

    @width.setter  # setter width with value
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property  # create property heighit
    def height(self):
        return self.__height

    @height.setter  # setter height with value
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
