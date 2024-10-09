#!/usr/bin/python3


"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of list of int/float): The matrix to divide.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to zero.

    Returns:
        list of list of floats: A new matrix with the results of the division.
    """

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                                                "of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")


    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")


    if div == 0:
        raise ZeroDivisionError("division by zero")


    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
