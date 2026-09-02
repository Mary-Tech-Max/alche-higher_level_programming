#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
