#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module defines a single function, matrix_divided, which divides
every element of a matrix (a list of lists of ints/floats) by a given
divisor and returns a new matrix with the results rounded to 2 decimal
places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix: a list of lists of integers or floats. Each row must
            be the same length.
        div: the integer or float divisor.

    Returns:
        A new matrix (list of lists) with each element of matrix
        divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats.
        TypeError: if the rows of matrix are not all the same size.
        TypeError: if div is not an integer or a float.
        ZeroDivisionError: if div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for element in row:
            if not isinstance(element, (int, float)) or isinstance(
                    element, bool):
                raise TypeError(err_matrix)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(err_size)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
