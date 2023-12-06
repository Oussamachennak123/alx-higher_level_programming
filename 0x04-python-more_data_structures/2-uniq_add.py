#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = []
    somme = 0
    for x in my_list:
        if x not in add:
            somme = somme + 1
            add.append(x)
    return somme
