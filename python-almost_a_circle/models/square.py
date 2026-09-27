#!/usr/bin/python3
"""Module that defines the Square class.

This module defines Square, a class that represents a square and
inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special Rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size: the size of the square (used as both width and
                height), must be an integer > 0.
            x: the x coordinate of the square, must be an
                integer >= 0. Defaults to 0.
            y: the y coordinate of the square, must be an
                integer >= 0. Defaults to 0.
            id: the id to assign to this instance, passed to
                Rectangle/Base.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Assigns width and height (in that order) to value, using the
        same validation as Rectangle's width setter.

        Args:
            value: the new size, must be an integer > 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes using no-keyword or keyword arguments.

        Args:
            *args: new attribute values in this order: id, size, x,
                y. If *args is not empty, **kwargs is ignored
                entirely.
            **kwargs: new attribute values as key/value pairs, used
                only if *args is empty.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
