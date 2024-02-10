#!/usr/bin/python3
"""define function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """user load for create object json"""
    with open(filename, 'r') as f:
        return json.load(f)
