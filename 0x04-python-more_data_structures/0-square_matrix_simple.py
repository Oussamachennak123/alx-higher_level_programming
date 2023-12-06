#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(run) for run in matrix]
    for a in range(len(new_matrix)):
        for b in range(len(new_matrix[a])):
            new_matrix[a][b] *= new_matrix[a][b]
    return new_matrix
