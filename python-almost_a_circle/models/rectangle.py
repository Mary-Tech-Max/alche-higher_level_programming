#!/usr/bin/python3
"""Module that defines the Rectangle class.

This module defines Rectangle, a class that represents a rectangle
and inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle, inheriting id management from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width: the width of the rectangle, must be an integer > 0.
            height: the height of the rectangle, must be an
                integer > 0.
            x: the x coordinate of the rectangle, must be an
                integer >= 0. Defaults to 0.
            y: the y coordinate of the rectangle, must be an
                integer >= 0. Defaults to 0.
            id: the id to assign to this instance, passed to Base.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value: the new width, must be an integer > 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value: the new height, must be an integer > 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle.

        Args:
            value: the new x coordinate, must be an integer >= 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is negative.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle.

        Args:
            value: the new y coordinate, must be an integer >= 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is negative.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle to stdout using the # character.

        The rectangle is offset from the top and left of the screen
        by y and x blank lines/spaces respectively.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes using no-keyword or keyword arguments.

        Args:
            *args: new attribute values in this order: id, width,
                height, x, y. If *args is not empty, **kwargs is
                ignored entirely.
            **kwargs: new attribute values as key/value pairs, used
                only if *args is empty.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
