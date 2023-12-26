#!/usr/bin/python3
""" define a class Square like 0-square"""


class Square():
    """ class square """
    def __init__(self, __size=0):

        @property  # create the property
        def size(self):
            return self.__size
        """ define the propert """

        @size.setter  # create the setter
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):  # déclarer self comme parametre
        return (self.__size ** 2)  # puissance 2

