#!/usr/bin/python3
"""Defines a custom list class."""


class MyList(list):
    """A list with a method that prints a sorted copy."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
