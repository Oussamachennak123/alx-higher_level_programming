#!/usr/bin/python3
"""
define function for returns the dictionary description
with simple data structure
(list, dictionary, string, integer and boolean)
"""


def class_to_json(obj):
    """obj Class: list, dictionary, string, integer and boolean """
    return obj.__dict__
