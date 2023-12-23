"""
Unit tests for lc0242_valid_anagram.py
"""

import unittest
from typing import Callable

from leetcode.lc0242_valid_anagram import is_anagram1, is_anagram2


class TestIsAnagram(unittest.TestCase):
    """Unit Tests for lc242_valid_anagram.py"""

    def setUp(self) -> None:
        # Define test cases as tuples of arguments and expected results
        self.test_cases = [
            (("anagram", "nagaram"), True),
            (("rat", "car"), False),
            (("rat", "car"), False),
            (("a", "ab"), False),
        ]

    def run_test_case(self, is_anagram_func: Callable[..., bool]):
        """Helper function to run test cases for a specific isAnagram function"""
        # Iterate over the test cases
        for args, expected_result in self.test_cases:
            # Use subTest context manager to run a test w/ multiple subtests
            # Used to prevent test cases from stopping after the first failure
            with self.subTest(args=args):
                # Call the specified isAnagram function with the test case arguments
                result = is_anagram_func(*args)
                # Assert that the result matches the expected result
                self.assertEqual(result, expected_result)

    def test_is_anagram1(self):
        """Test cases for isAnagram1: Brute Force Approach"""
        # Run the test cases for isAnagram1 using the helper function
        self.run_test_case(is_anagram1)

    def test_is_anagram2(self):
        """Test cases for isAnagram2: Brute Force Approach"""
        # Run the test cases for isAnagram2 using the helper function
        self.run_test_case(is_anagram2)


# Run the test suite if this script is executed directly
if __name__ == "__main__":
    unittest.main()
