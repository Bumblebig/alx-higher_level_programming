#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""

    # checks if the matrix is a list of list
    if not isinstance(matrix, list) or not all(isinstance(row, list) and not all(isinstance(el, (int, float)) for el in row)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # checks whether rows all have the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # checks whether div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # checks if div is equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # divide all elements of matrix by div
    new_mat = [[round(el/div, 2) for el in row] for row in matrix]

    return new_mat
