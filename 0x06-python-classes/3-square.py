#!/usr/bin/python3
""" define a class Square like 0-square"""


class Square():
    """ class square """
    def __init__(self, __size=0):
        if (__size) != int:   # check if size is int
            raise TypeError("size must be an integer")
        elif __size < 0:   # check if size is positive
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):  # déclarer self comme parametre
        return (self.__size ** 2)  # puissance 2
