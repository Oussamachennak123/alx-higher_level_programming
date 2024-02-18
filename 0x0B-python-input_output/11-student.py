#!/usr/bin/python3
""" define class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        My_dict = {}
        for i in attrs:
            if hasattr(self, i):
                My_dict[i] = getattr(self, i)
        return My_dict

    def reload_from_json(self, json):
        for kay, value in json.items():
            setattr(self, kay, value)
