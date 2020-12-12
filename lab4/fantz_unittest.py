import unittest

from fantz import find_min_number


class TestAlgorithmResult(unittest.TestCase):
    def test_results(self):
        # Test the results when the input values are positive numbers from 1 to 99
        self.assertAlmostEqual(find_min_number('101101101', '5'), 3)
        self.assertAlmostEqual(find_min_number('1111101', '5'), 1)
        self.assertAlmostEqual(find_min_number('110011011', '5'), 3)
        self.assertAlmostEqual(find_min_number('101101100100000000000011001010001000000001101100000010001000101100000000000000',
                                               '12'), 5)

    def test_values(self):
        # Make sure the value errors are raised when necessary
        with self.assertRaises(ValueError):
            find_min_number('101101101', '0')
        with self.assertRaises(ValueError):
            find_min_number('101101101', '100')
        with self.assertRaises(ValueError):
            find_min_number('', '10')
        with self.assertRaises(ValueError):
            find_min_number('10011101111010010011111011001110010100011110010111001000110011101111'
                            '0100100111110110011100101000110010110000111100101110010001', '10')


    def test_types(self):
        # Make sure the type errors are raised when necessary
        with self.assertRaises(TypeError):
            find_min_number('110011011', 'I am an impostor')
        with self.assertRaises(TypeError):
            find_min_number('91010101010', '2')

