#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for value in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, value)))
    return new_matrix
