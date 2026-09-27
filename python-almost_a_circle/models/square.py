#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square.__init__."""

    def test_inherits_from_rectangle(self):
        """Square is a subclass of Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_width_equals_height(self):
        """A Square's width and height are always equal to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_explicit_x_y_id(self):
        """x, y and id are set correctly when provided."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 12)

    def test_no_new_attributes(self):
        """Square doesn't create attributes beyond Rectangle's."""
        s = Square(5)
        expected = {
            "_Rectangle__width", "_Rectangle__height",
            "_Rectangle__x", "_Rectangle__y", "id"
        }
        self.assertEqual(set(s.__dict__.keys()), expected)


class TestSquareValidation(unittest.TestCase):
    """Tests that Square inherits Rectangle's validation."""

    def test_size_not_int(self):
        """Non-integer size raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_zero(self):
        """Size of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        """Negative size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_x_negative(self):
        """Negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)


class TestSquareArea(unittest.TestCase):
    """Tests for Square.area (inherited from Rectangle)."""

    def test_area(self):
        """area returns size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str_format(self):
        """__str__ returns the expected formatted string."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] ({}) 0/0 - 5".format(s.id))

    def test_str_with_position(self):
        """__str__ correctly shows a non-default position."""
        s = Square(3, 1, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 1/3 - 3")


class TestSquareSize(unittest.TestCase):
    """Tests for the Square.size property."""

    def test_size_getter(self):
        """size getter returns width (== height)."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """size setter updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)

    def test_size_setter_invalid_type(self):
        """size setter uses width's validation for type errors."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_invalid_value(self):
        """size setter uses width's validation for value errors."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square.update with *args."""

    def test_update_id_only(self):
        """update(id) changes only the id."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_all_positional(self):
        """update(id, size, x, y) sets all attributes."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_no_args(self):
        """update() with no arguments changes nothing."""
        s = Square(5, id=1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square.update with **kwargs."""

    def test_update_kwargs(self):
        """update(**kwargs) sets attributes by name."""
        s = Square(5, id=1)
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 0/1 - 7")

    def test_args_take_priority_over_kwargs(self):
        """If *args is not empty, **kwargs is ignored."""
        s = Square(5, id=1)
        s.update(2, size=99)
        self.assertEqual(s.id, 2)
        self.assertNotEqual(s.size, 99)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_to_dictionary_keys_and_values(self):
        """to_dictionary returns the correct dict."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_round_trip(self):
        """update(**to_dictionary()) reproduces an equal square."""
        s1 = Square(10, 2, 1, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
