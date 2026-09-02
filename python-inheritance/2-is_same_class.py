#!/usr/bin/python3
"""Provides a function to check an object's exact class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    return type(obj) is a_class
