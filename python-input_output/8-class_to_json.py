#!/usr/bin/python3
"""Returns an object's dictionary for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object."""
    return obj.__dict__
