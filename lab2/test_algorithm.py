import unittest

from algorithm import find_side_lenght


class TestAlgorithmResult(unittest.TestCase):
    def test_results(self):
        # Test the results when the input values are positive numbers
        self.assertAlmostEqual(find_side_lenght(10, 2, 3), 9)
        self.assertAlmostEqual(find_side_lenght(2, 1000000000, 999999999), 1999999998)
        self.assertAlmostEqual(find_side_lenght(4, 1, 1), 2)

    def test_values(self):
        # Make sure the value errors are raised when necessary
        with self.assertRaises(ValueError):
            find_side_lenght(-1, 1, 1)
            find_side_lenght(1, -1, 1)
            find_side_lenght(1, 1, -1)

    def test_types(self):
        # Make sure the type errors are raised when necessary
        with self.assertRaises(TypeError):
            find_side_lenght('imposter', 1, 1)
            find_side_lenght(1, True, 1)
            find_side_lenght(1, 1, 2 + 3j)
