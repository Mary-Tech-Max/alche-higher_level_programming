#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle.__init__."""

    def test_inherits_from_base(self):
        """Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_basic_attributes(self):
        """width, height, x, y are set correctly."""
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_auto_assigned(self):
        """id is auto-assigned when not provided."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int_type(self):
        """Non-integer width raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_float(self):
        """Float width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10.5, 2)

    def test_width_bool(self):
        """Boolean width raises TypeError (bool is not a plain int)."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_height_not_int_type(self):
        """Non-integer height raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_zero(self):
        """Width of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """Negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero(self):
        """Height of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        """Negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_not_int(self):
        """Non-integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 0)

    def test_x_negative(self):
        """Negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)

    def test_y_not_int(self):
        """Non-integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "a")

    def test_y_negative(self):
        """Negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_x_zero_is_valid(self):
        """x of exactly 0 is a valid value."""
        r = Rectangle(10, 2, 0, 0)
        self.assertEqual(r.x, 0)

    def test_setter_width_invalid(self):
        """Setting width to an invalid value raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_setter_x_invalid_type(self):
        """Setting x to an invalid type raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area_basic(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_return_type(self):
        """area returns an integer."""
        self.assertIsInstance(Rectangle(3, 2).area(), int)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def test_display_basic(self, ):
        """display prints a grid of # with no offset."""
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """display accounts for x and y offsets."""
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 1, 1, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str_format(self):
        """__str__ returns the expected formatted string."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_x_y(self):
        """__str__ with default x/y."""
        r = Rectangle(5, 5, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 5/5")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for Rectangle.update with *args."""

    def test_update_id_only(self):
        """update(id) changes only the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_all_positional(self):
        """update(id, width, height, x, y) sets all attributes."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        """update() with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for Rectangle.update with **kwargs."""

    def test_update_kwargs(self):
        """update(**kwargs) sets attributes by name."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_kwargs_multiple(self):
        """update(**kwargs) with several keys at once."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_args_take_priority_over_kwargs(self):
        """If *args is not empty, **kwargs is ignored."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(2, height=99)
        self.assertEqual(r.id, 2)
        self.assertNotEqual(r.height, 99)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_to_dictionary_keys_and_values(self):
        """to_dictionary returns the correct dict."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        )

    def test_to_dictionary_round_trip(self):
        """update(**to_dictionary()) reproduces an equal rectangle."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
