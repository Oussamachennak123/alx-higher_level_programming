#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.

    Args:
        my_list (list): list of all elements.
        x (int): the number of time you need to iterate over the list
    Return:
        The number of elements printed.
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
