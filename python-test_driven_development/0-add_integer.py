#!/usr/bin/python3
"""Module that adds two integers.

This module defines a single function, add_integer, which adds two
numbers together after casting any floats to integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats.

    Args:
        a: the first number, must be an int or a float.
        b: the second number, must be an int or a float (default 98).

    Returns:
        The integer sum of a and b, after casting floats to ints.

    Raises:
        TypeError: if a is not an int or float.
        TypeError: if b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
