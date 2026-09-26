#!/usr/bin/python3
"""Module that prints a square made of the ``#`` character.

This module defines a single function, print_square, which prints a
square of a given size using the ``#`` character.
"""


def print_square(size):
    """Print a square with the character ``#``.

    Args:
        size: the size length of the square, must be an integer.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
