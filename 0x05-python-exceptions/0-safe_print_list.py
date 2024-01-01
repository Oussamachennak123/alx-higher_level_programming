#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - a function that prints <x>
    element of <my_list>
    """
    Suivant = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            Suivant += 1
        print()
    except IndexError as e:
        print(f"Erreur : {e}")
    return Suivant
