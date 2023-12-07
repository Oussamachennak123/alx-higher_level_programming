#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    tier_key = dict(sorted(a_dictionary.key()))
    new_dictionary = {key: a_dictionary[key] for key in tier_key}
    print("{}".format(new_dictionary))
