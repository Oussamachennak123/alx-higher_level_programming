#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)
    od_set = set(set_1 | set_2)
    return od_set
