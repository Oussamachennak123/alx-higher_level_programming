#!/usr/bin/python3
class MyList(list):
    """define class MyList that inherits from list"""
    def print_sorted(self):
        """define fontion print_sorted"""
        print(sorted(self))
