#!/usr/bin/python3
"""Writes Python objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
