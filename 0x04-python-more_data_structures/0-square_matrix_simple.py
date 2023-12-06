#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for run in matrix:
        new_matrix = [list(run)]
    for a in range(len(new_matrix)):
        for b in range(len(new_matrix[a])):
            new_matrix[a][b] *= new_matrix[a][b]
    return new_matrix
