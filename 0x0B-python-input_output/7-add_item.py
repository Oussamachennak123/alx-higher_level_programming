#!/usr/bin/python3
"""define function that writes an Object to a text file using a JSON"""
import sys


if __name__ == "__main__":
    """ import function save to json and load_from_jason"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
