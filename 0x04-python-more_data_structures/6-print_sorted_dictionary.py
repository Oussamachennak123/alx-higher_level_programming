#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    tier_keys = dict(sorted(a_dictionary.items()))
    for a, b in tier_keys.items():
        print('{}: {}'.format(a, b))
