#!/usr/bin/python3
"""
Module: matrix_operations

This module provides functions to perform various operations on 2D matrices.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (List[List[int]]): A square 2D matrix as a list of lists.

    Raises:
        ValueError: If the matrix is not square

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6],
        ...     [7, 8, 9]
        ... ]
        >>> rotate_2d_matrix(matrix)
        >>> matrix
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
    """
    if not matrix or not matrix[0]:
        raise ValueError("The matrix must be non-empty.")

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        raise ValueError("Only square matrices can be rotated.")

    rotated_copy = list(zip(*matrix[::-1]))
    for row in range(num_rows):
        for col in range(num_cols):
            matrix[row][col] = rotated_copy[row][col]
