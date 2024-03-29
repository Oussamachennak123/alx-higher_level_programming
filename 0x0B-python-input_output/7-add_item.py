#!/usr/bin/python3
"""add all arguments to a python list and save them in a file"""
import sys

if __name__ == "__main__":  # verifier if script is principal or not
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        m_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        m_list = []
    m_list.extend(sys.argv[1:])
    save_to_json_file(m_list, "add_item.json")
