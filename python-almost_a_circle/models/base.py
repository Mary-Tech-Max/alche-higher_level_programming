#!/usr/bin/python3
"""Module that defines the Base class.

This module defines Base, the base class for all other classes in
this project. It manages the id attribute for every instance created
from a class that inherits from it, and provides JSON
serialization/deserialization helpers shared by all subclasses.
"""
import json


class Base:
    """Base class that manages the id attribute of all future classes.

    This class avoids duplicating the id-management logic (and by
    extension, the same bugs) in every class that needs an id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id: the id to assign to this instance. If None, a new
                unique id is generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries: a list of dictionaries.

        Returns:
            The JSON string representation of list_dictionaries, or
            "[]" if list_dictionaries is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        The file is named <Class name>.json (for example
        Rectangle.json) and is overwritten if it already exists.

        Args:
            list_objs: a list of instances that inherit from Base. If
                None, an empty list is saved instead.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string: a string representing a list of dictionaries.

        Returns:
            The list represented by json_string, or an empty list if
            json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of cls with all attributes already set.

        A "dummy" instance is created with mandatory attributes set
        to placeholder values, then updated with the real values from
        dictionary.

        Args:
            dictionary: key/value pairs of attributes to set on the
                new instance.

        Returns:
            A new instance of cls with its attributes set from
            dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json.

        Returns:
            A list of instances of cls, built from the JSON file
            <Class name>.json. If that file doesn't exist, an empty
            list is returned.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**d) for d in list_dicts]
