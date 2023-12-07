#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    tier_keys = dict(sorted(a_dictionary.items()))
    new_dictionary = {key: a_dictionary[key] for key in tier_keys}
    print("{}".format(new_dictionary))
