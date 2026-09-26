#!/usr/bin/python3
"""Module that prints a text with indentation after ``.``, ``?`` and ``:``.

This module defines a single function, text_indentation, which adds
two new lines after each occurrence of ``.``, ``?`` or ``:``.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each ``.``, ``?`` and ``:``.

    Args:
        text: the string to print, must be a string.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ".?:"
    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in special_chars:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
