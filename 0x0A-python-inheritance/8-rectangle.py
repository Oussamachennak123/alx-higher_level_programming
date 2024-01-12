#!/usr/bin/python3
"""Definebclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):  # utiliser class BaseGemetry
    def __init__(self, width, height):
        """ new rectangle user"""
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)
        self.__width = width
        self.__height = height
