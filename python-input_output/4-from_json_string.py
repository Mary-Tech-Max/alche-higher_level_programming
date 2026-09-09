#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string."""
    return json.loads(my_str)
