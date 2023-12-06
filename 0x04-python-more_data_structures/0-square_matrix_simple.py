#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for k in range(len(new_matrix)):
        new_matrix[k] = list(map(lambda x: x ** 2, new_matrix[k]))
    return new_matrix
