#!/usr/bin/python3
"""Unittest for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base.__init__ id management."""

    def test_id_auto_assigned_first(self):
        """First auto-assigned id continues the shared counter."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_explicit(self):
        """An explicit id is used as-is."""
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_id_none_increments_counter(self):
        """Passing None still auto-generates an id."""
        b1 = Base(None)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_no_args(self):
        """Base() with no arguments doesn't raise."""
        try:
            Base()
        except Exception:
            self.fail("Base() raised unexpectedly")


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        """None returns the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list returns the string '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """A list of dicts is converted to valid JSON."""
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(result), list_dicts)

    def test_return_type(self):
        """to_json_string always returns a string."""
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        """None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """A valid JSON string round-trips to the same list."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_round_trip_with_to_json_string(self):
        """to_json_string and from_json_string are inverses."""
        list_dicts = [{"id": 1, "width": 3}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created by the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_rectangles(self):
        """save_to_file writes the correct JSON to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_none(self):
        """save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites_existing_file(self):
        """save_to_file overwrites any existing file."""
        Rectangle.save_to_file([Rectangle(1, 1, id=1)])
        Rectangle.save_to_file([Rectangle(2, 2, id=2)])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]["id"], 2)

    def test_save_squares_filename(self):
        """save_to_file uses <ClassName>.json as the filename."""
        Square.save_to_file([Square(3, id=1)])
        self.assertTrue(os.path.exists("Square.json"))


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        """create builds a Rectangle with the given attributes."""
        r1 = Rectangle(3, 5, 1, id=99)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """create builds a Square with the given attributes."""
        s1 = Square(5, 1, 2, id=99)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created by the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_no_file_returns_empty_list(self):
        """If the file doesn't exist, an empty list is returned."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_then_load_rectangles(self):
        """Loading after saving returns equivalent Rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))

    def test_save_then_load_squares(self):
        """Loading after saving returns equivalent Squares."""
        s1 = Square(5, id=5)
        s2 = Square(7, 9, 1, id=6)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(s1))
        self.assertEqual(str(loaded[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
