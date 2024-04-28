#!/usr/bin/python3
"""Defines a peak-finding algorithm"""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    lengthl = len(list_of_integers)
    m = int(lengthl / 2)
    lim = list_of_integers

    if m - 1 < 0 and m + 1 >= lengthl:
        return lim[m]
    elif m - 1 < 0:
        return lim[m] if li[m] > lim[m + 1] else lim[m + 1]
    elif m + 1 >= lengthl:
        return lim[m] if lim[m] > lim[m - 1] else lim[m - 1]

    if lim[m - 1] < lim[m] > lim[m + 1]:
        return lim[m]

    if lim[m + 1] > lim[m - 1]:
        return find_peak(lim[m:])
    return find_peak(lim[:m])
