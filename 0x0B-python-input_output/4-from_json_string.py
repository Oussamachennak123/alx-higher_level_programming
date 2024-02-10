#!/usr/bin/python3
"""devine function returns an object(Python data structure) by a JSON"""
import json


def from_json_string(my_str):
    """ user load for convered python data structure"""
    return json.loads(my_str)
