#!/usr/bin/python3
def best_score(a_dictionary):
    key_max = max(a_dictionary, key = lambda k: a_dictionary[k])
    return key_max
