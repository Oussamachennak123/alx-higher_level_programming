#!/usr/bin/python3

def uniq_add(my_list=[]):
    add = []
    somme = 0
    for a in my_list:
        if a not in add:
            somme += 1
            add.append(a)
    return somme
