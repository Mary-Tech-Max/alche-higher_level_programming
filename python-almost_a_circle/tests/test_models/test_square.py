#!/usr/bin/python3
"""Unittest for the Square class."""
import os
import unittest
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for valid Square instantiation."""

    def test_square_1(self):
        """Test of Square(1)."""
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y), (1, 0, 0))

    def test_square_1_2(self):
        """Test of Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_square_1_2_3(self):
        """Test of Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_square_1_2_3_4(self):
        """Test of Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))


class TestSquareTypeErrors(unittest.TestCase):
    """Tests for Square TypeError validation."""

    def test_square_str_size(self):
        """Test of Square("1")."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_str_x(self):
        """Test of Square(1, "2")."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_str_y(self):
        """Test of Square(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")


class TestSquareValueErrors(unittest.TestCase):
    """Tests for Square ValueError validation."""

    def test_square_negative_size(self):
        """Test of Square(-1)."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        """Test of Square(1, -2)."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        """Test of Square(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        """Test of Square(0)."""
        with self.assertRaises(ValueError):
            Square(0)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str(self):
        """Test of __str__() for Square."""
        s = Square(3, 1, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 1/3 - 3")


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_to_dictionary(self):
        """Test of to_dictionary() in Square."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(
            s.to_dictionary(), {"id": 1, "size": 10, "x": 2, "y": 1}
        )


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square.update with *args."""

    def test_update_no_args(self):
        """Test of update() in Square."""
        s = Square(5, 1, 1, 1)
        s.update()
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 5, 1, 1))

    def test_update_89(self):
        """Test of update(89) in Square."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """Test of update(89, 1) in Square."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_89_1_2(self):
        """Test of update(89, 1, 2) in Square."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Square."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square.update with **kwargs."""

    def test_update_kwargs_id(self):
        """Test of update(**{'id': 89}) in Square."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test of update(**{'id': 89, 'size': 1}) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        """update(**{'id': 89, 'size': 1, 'x': 2}) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_id_size_x_y(self):
        """update(**{...,'x': 2, 'y': 3}) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))


class TestSquareCreate(unittest.TestCase):
    """Tests for Square.create."""

    def test_create_id(self):
        """Test of Square.create(**{'id': 89}) in Square."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Square.create(**{'id': 89, 'size': 1}) in Square."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        """create(**{'id': 89, 'size': 1, 'x': 2}) in Square."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_id_size_x_y(self):
        """create(**{...,'x': 2, 'y': 3}) in Square."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))


class TestSquareSaveLoadFile(unittest.TestCase):
    """Tests for Square.save_to_file and load_from_file."""

    def tearDown(self):
        """Remove Square.json after each test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Square.save_to_file([]) in Square."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Test of Square.save_to_file([Square(1)]) in Square."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertNotEqual(f.read(), "[]")

    def test_load_from_file_no_file(self):
        """load_from_file() when file doesn't exist, in Square."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_existing(self):
        """load_from_file() when file exists, in Square."""
        s = Square(1)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(s))


if __name__ == "__main__":
    unittest.main()
