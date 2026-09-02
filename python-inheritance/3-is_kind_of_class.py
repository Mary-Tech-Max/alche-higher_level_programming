#!/usr/bin/python3
"""Provides a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of or inherits from a_class."""
    return isinstance(obj, a_class)
