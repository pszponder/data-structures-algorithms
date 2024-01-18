"""
Unit tests for linear_search.py
"""

import unittest
from typing import Callable

from data_structures.search.linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    """Unit Tests"""

    def setUp(self) -> None:
        # Define test cases as tuples of args & expected results
        self.test_cases = [
            (([0, 1, 2, 3], 0), 0),
            (([0, 1, 2, 3], 1), 1),
            (([0, 1, 2, 3], 2), 2),
            (([0, 1, 2, 3], 3), 3),
            (([0, 1, 2, 3], 10), -1),
        ]

    def run_test_case(self, fut: Callable[..., int]):
        """Helper function to run test cases for a specific callable function"""
        # Iterate over the test cases
        for args, expected_result in self.test_cases:
            # Use subTest context manager to run a test w/ multiple subtests
            # Used to prevent test cases from stopping after the first failure
            with self.subTest(args=args):
                # Call the specified function under test with the test case arguments
                result = fut(*args)
                # Assert that the result matches the expected result
                self.assertEqual(result, expected_result)

    def test_linear_search(self):
        """Test cases"""
        self.run_test_case(linear_search)
