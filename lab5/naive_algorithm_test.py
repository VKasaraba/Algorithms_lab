import unittest

from naive_algorithm import find_substring_positions


# execute: python -m unittest naive_algorithm_test

class TestAlgorithmResult(unittest.TestCase):
    def test_results(self):
        # Test the results when the input types and values are correct
        self.assertListEqual(find_substring_positions('rrFrr', 'r'), [0, 1, 3, 4])
        self.assertListEqual(find_substring_positions('ABC-DE-FG', 'de'), [4])
        self.assertListEqual(find_substring_positions('1', '1'), [0])
        self.assertListEqual(find_substring_positions('We will rock you', 'Queen'), [])
        self.assertListEqual(find_substring_positions('aaaaab', 'aa'), [0, 1, 2, 3])
        self.assertListEqual(find_substring_positions('Volodymyr Volodymyrovych', 'Volodymyr'), [0, 10])

    def test_values(self):
        # Make sure the value errors are raised when necessary
        with self.assertRaises(ValueError):
            find_substring_positions('t', 'tt')
        with self.assertRaises(ValueError):
            find_substring_positions('', 't')
        with self.assertRaises(ValueError):
            find_substring_positions('t', '')
        with self.assertRaises(ValueError):
            find_substring_positions('', '')

    def test_types(self):
        # Make sure the type errors are raised when necessary
        with self.assertRaises(TypeError):
            find_substring_positions(1, 't')
        with self.assertRaises(TypeError):
            find_substring_positions('t', 1)
        with self.assertRaises(TypeError):
            find_substring_positions(True, 't')
        with self.assertRaises(TypeError):
            find_substring_positions(['impostor'], 't')
        with self.assertRaises(TypeError):
            find_substring_positions('t', 2 + 3j)
