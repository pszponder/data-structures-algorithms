"""
Unit tests for lc217_contains_duplicate.py
"""

import unittest

from leetcode.lc217_contains_duplicate import (
    contains_duplicate0,
    contains_duplicate1,
    contains_duplicate2,
    contains_duplicate3,
)


class TestContainsDuplicate(unittest.TestCase):
    """Unit tests for contains_duplicate.py"""

    def setUp(self) -> None:
        # Define lists for testing
        self.list1 = [1, 2, 3, 1]
        self.list2 = [1, 2, 3, 4]
        self.list3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    def test_contains_duplicate0(self):
        """Test cases for contains_duplicate0 function: Brute Force approach"""
        self.assertTrue(contains_duplicate0(self.list1))
        self.assertFalse(contains_duplicate0(self.list2))
        self.assertTrue(contains_duplicate0(self.list3))

    def test_contains_duplicate1(self):
        """Test cases for contains_duplicate1 function: Map approach"""
        self.assertTrue(contains_duplicate1(self.list1))
        self.assertFalse(contains_duplicate1(self.list2))
        self.assertTrue(contains_duplicate1(self.list3))

    def test_contains_duplicate2(self):
        """Test cases for contains_duplicate2 function: Sorting approach"""
        self.assertTrue(contains_duplicate2(self.list1))
        self.assertFalse(contains_duplicate2(self.list2))
        self.assertTrue(contains_duplicate2(self.list3))

    def test_contains_duplicate3(self):
        """Test cases for contains_duplicate3 function: Set Approach"""
        self.assertTrue(contains_duplicate3(self.list1))
        self.assertFalse(contains_duplicate3(self.list2))
        self.assertTrue(contains_duplicate3(self.list3))


if __name__ == "__main__":
    unittest.main()
