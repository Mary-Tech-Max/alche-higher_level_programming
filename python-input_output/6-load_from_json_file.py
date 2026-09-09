#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
