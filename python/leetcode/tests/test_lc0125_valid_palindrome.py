"""
Unit tests for lc0001_two_sum.py
"""

import unittest
from typing import Callable

from leetcode.lc0125_valid_palindrome import (
    is_palindrome1,
    is_palindrome2,
    is_palindrome3,
)


class TestIsPalindrome(unittest.TestCase):
    """Unit Tests for lc0125_valid_palindrome.py"""

    def setUp(self) -> None:
        # Define test cases as tuples of args & expected results
        self.test_cases = [
            (("A man, a plan, a canal: Panama",), True),
            (("race a car",), False),
            ((" ",), True),
            (("0P",), False),
        ]

    def run_test_case(self, fut: Callable[[str], bool]):
        """Helper function to run test cases for a specific function"""
        # Iterate over the test cases
        for args, expected_result in self.test_cases:
            # Use subTest context manager to run a test w/ multiple subtests
            # Used to prevent test cases from stopping after the first failure
            with self.subTest(args=args):
                # Call the specified function under test with the test case arguments
                result = fut(*args)
                # Assert that the result matches the expected result
                self.assertEqual(result, expected_result)

    def test_is_palindrome1(self):
        """Test cases for is_palindrome1: 2-Pointers"""
        self.run_test_case(is_palindrome1)

    def test_is_palindrome2(self):
        """Test cases for is_palindrome2: 2-Pointers"""
        self.run_test_case(is_palindrome2)

    def test_is_palindrome3(self):
        """Test cases for is_palindrome3: 2-Pointers"""
        self.run_test_case(is_palindrome3)
