#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import io
import os
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for valid Rectangle instantiation."""

    def test_rectangle_1_2(self):
        """Test of Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_rectangle_1_2_3(self):
        """Test of Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_rectangle_1_2_3_4(self):
        """Test of Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_rectangle_1_2_3_4_5(self):
        """Test of Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))


class TestRectangleTypeErrors(unittest.TestCase):
    """Tests for Rectangle TypeError validation."""

    def test_rectangle_str_width(self):
        """Test of Rectangle("1", 2)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_str_height(self):
        """Test of Rectangle(1, "2")."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_str_x(self):
        """Test of Rectangle(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_str_y(self):
        """Test of Rectangle(1, 2, 3, "4")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")


class TestRectangleValueErrors(unittest.TestCase):
    """Tests for Rectangle ValueError validation."""

    def test_rectangle_negative_width(self):
        """Test of Rectangle(-1, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        """Test of Rectangle(1, -2)."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        """Test of Rectangle(0, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        """Test of Rectangle(1, 0)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        """Test of Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        """Test of Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area(self):
        """Test of area()."""
        self.assertEqual(Rectangle(3, 2).area(), 6)


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str(self):
        """Test of __str__() for Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def test_display_without_x_and_y(self):
        """Test of display() without x and y."""
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        """Test of display() without y."""
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display_with_x_and_y(self):
        """Test of display()."""
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 1, 1, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n")


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_to_dictionary(self):
        """Test of to_dictionary() in Rectangle."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        )


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for Rectangle.update with *args."""

    def test_update_no_args(self):
        """Test of update() in Rectangle."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        attrs = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(attrs, (1, 10, 10, 10, 10))

    def test_update_89(self):
        """Test of update(89) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test of update(89, 1) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_89_1_2(self):
        """Test of update(89, 1, 2) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_89_1_2_3_4(self):
        """Test of update(89, 1, 2, 3, 4) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        attrs = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(attrs, (89, 1, 2, 3, 4))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for Rectangle.update with **kwargs."""

    def test_update_kwargs_id(self):
        """Test of update(**{'id': 89}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test of update(**{'id': 89, 'width': 1}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_id_width_height(self):
        """update(**{'id': 89, 'width': 1, 'height': 2}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_id_width_height_x(self):
        """update(**{...,'x': 3}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_id_width_height_x_y(self):
        """update(**{...,'x': 3, 'y': 4}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })
        attrs = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(attrs, (89, 1, 2, 3, 4))


class TestRectangleCreate(unittest.TestCase):
    """Tests for Rectangle.create."""

    def test_create_id(self):
        """Test of Rectangle.create(**{'id': 89}) in Rectangle."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Rectangle.create(**{'id': 89, 'width': 1}) in Rectangle."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_id_width_height(self):
        """create(**{'id':89,'width':1,'height':2}) in Rectangle."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_id_width_height_x(self):
        """create(**{...,'x': 3}) in Rectangle."""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_create_id_width_height_x_y(self):
        """create(**{...,'x': 3, 'y': 4}) in Rectangle."""
        r = Rectangle.create(**{
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })
        attrs = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(attrs, (89, 1, 2, 3, 4))


class TestRectangleSaveLoadFile(unittest.TestCase):
    """Tests for Rectangle.save_to_file and load_from_file."""

    def tearDown(self):
        """Remove Rectangle.json after each test."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test of Rectangle.save_to_file(None) in Rectangle."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Rectangle.save_to_file([]) in Rectangle."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertNotEqual(f.read(), "[]")

    def test_load_from_file_no_file(self):
        """load_from_file() when file doesn't exist, in Rectangle."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existing(self):
        """load_from_file() when file exists, in Rectangle."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(r))


if __name__ == "__main__":
    unittest.main()
