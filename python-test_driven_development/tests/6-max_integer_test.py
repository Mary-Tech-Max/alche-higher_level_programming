#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """Test with a list already in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list in no particular order"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test with a list in descending order"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list, should return None"""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test calling the function with no arguments"""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_sign_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_all_same_values(self):
        """Test with a list where all elements are equal"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)


if __name__ == '__main__':
    unittest.main()
