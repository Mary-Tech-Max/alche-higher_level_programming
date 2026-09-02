#!/usr/bin/python3
"""This module defines a function to list an object's attributes."""


def lookup(obj):
    """Return a list of attributes and methods of an object."""
    return dir(obj)
