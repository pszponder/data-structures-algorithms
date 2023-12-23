"""
Unit tests for lc0001_two_sum.py
"""

import unittest
from typing import Callable

from leetcode.lc0001_two_sum import two_sum1, two_sum2, two_sum3


class TestTwoSum(unittest.TestCase):
    """Unit Tests for lc0001_two_sum.py"""

    def setUp(self) -> None:
        # Define test cases as tuples of args & expected results
        self.test_cases = [
            (([2, 7, 11, 15], 9), [0, 1]),
            (([3, 2, 4], 6), [1, 2]),
            (([3, 3], 6), [0, 1]),
            (([-1, -2, -3, -4, -5], -8), [2, 4]),
        ]

    def run_test_case(self, fut: Callable[..., list[int]]):
        """Helper function to run test cases for a specific isAnagram function"""
        # Iterate over the test cases
        for args, expected_result in self.test_cases:
            # Use subTest context manager to run a test w/ multiple subtests
            # Used to prevent test cases from stopping after the first failure
            with self.subTest(args=args):
                # Call the specified function under test with the test case arguments
                result = fut(*args)
                # Assert that the result matches the expected result
                self.assertEqual(result, expected_result)

    def test_two_sum1(self):
        """Test cases for two_sum1: Brute Force"""
        self.run_test_case(two_sum1)

    def test_two_sum2(self):
        """Test cases for two_sum2: 2-pointers"""
        self.run_test_case(two_sum2)

    def test_two_sum3(self):
        """Test cases for two_sum3: hash map"""
        self.run_test_case(two_sum3)
