#!/usr/bin/python3
"""This module defines a Square class with an area method."""


class Square:
    """Represent a square with a validated size and area method."""

    def __init__(self, size=0):
        """Initialize a square and validate its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
