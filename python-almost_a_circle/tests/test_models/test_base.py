#!/usr/bin/python3
"""Unittest for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseId(unittest.TestCase):
    """Tests for Base() automatic and explicit id assignment."""

    def test_base_auto_id(self):
        """Test of Base() for assigning automatically an ID."""
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_base_auto_id_increments(self):
        """Test of Base() assigning an ID + 1 of the previous."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_explicit_id(self):
        """Test of Base(89) saving the ID passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_to_json_string_none(self):
        """Test of Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test of Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_of_dicts(self):
        """Test of Base.to_json_string([{'id': 12}])."""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(json.loads(result), [{'id': 12}])

    def test_to_json_string_returns_string(self):
        """Test of Base.to_json_string([{'id': 12}]) returning a str."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_from_json_string_none(self):
        """Test of Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test of Base.from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        """Test of Base.from_json_string('[{ "id": 89 }]')."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Test of from_json_string('[{ "id": 89 }]') returning a list."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)


class TestBaseSaveLoadFile(unittest.TestCase):
    """Tests for Base.save_to_file / load_from_file (via subclasses)."""

    def tearDown(self):
        """Remove any JSON files created by the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_none(self):
        """Base.save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Base.save_to_file([]) writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one_object(self):
        """Base.save_to_file writes a list with one object's dict."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r.to_dictionary()])

    def test_load_from_file_no_file(self):
        """load_from_file() returns [] when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existing(self):
        """load_from_file() returns matching instances when file exists."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(r))


if __name__ == "__main__":
    unittest.main()
