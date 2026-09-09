#!/usr/bin/python3
"""Module for appending text to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 text file and return characters written."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
