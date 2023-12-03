#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix :
        for element in r :
            print('{:d}'.format(element), end=' ')
