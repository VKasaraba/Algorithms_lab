import unittest

from dejkstra_algorithm import find_min_distance


class TestAlgorithmResult(unittest.TestCase):
    def test_results(self):
        # Test the results when the input values are positive numbers
        self.assertAlmostEqual(find_min_distance(N1, C1, G1, M1), 10)
        self.assertAlmostEqual(find_min_distance(N2, C2, G2, M2), 100)
        self.assertAlmostEqual(find_min_distance(N3, C3, G3, M3), 1000000000)

    def test_values(self):
        # Make sure the value errors are raised when necessary
        with self.assertRaises(ValueError):
            find_min_distance(-1, [2], [[], [(2, 3)], [(1, 3)], []], 2)
        with self.assertRaises(ValueError):
            find_min_distance(3, [], [[], [(2, 3)], [(1, 3)], []], 2)
        with self.assertRaises(ValueError):
            find_min_distance(3, [2], [[], [(2, 3)], []], 2)
        with self.assertRaises(ValueError):
            find_min_distance(3, [2], [[], [(2, 3)], [(1, 3)], []], -1)

    def test_types(self):
        # Make sure the type errors are raised when necessary
        with self.assertRaises(TypeError):
            find_min_distance('I am an impostor', [2], [[], [(2, 3)], [(1, 3)], []], 2)
        with self.assertRaises(TypeError):
            find_min_distance(3, True, [[], [(2, 3)], [(1, 3)], []], 2)
        with self.assertRaises(TypeError):
            find_min_distance(3, [2], 2 + 3j, 2)
        with self.assertRaises(TypeError):
            find_min_distance(3, [2], [[], [(2, 3)], [(1, 3)], []], 2.2222)


N1 = 9
M1 = 12
C1 = [2, 4, 6]
G1 = [
    [],  # extra
    [(2, 20), (4, 20)],  # 1
    [(3, 20), (1, 20), (5, 10)],  # 2
    [(6, 20), (2, 20)],  # 3
    [(1, 20), (7, 20), (5, 10)],  # 4
    [(2, 10), (4, 10), (6, 10), (8, 10)],  # 5
    [(9, 20), (3, 20), (5, 10)],  # 6
    [(4, 20), (8, 20)],  # 7
    [(7, 20), (9, 20), (5, 10)],  # 8
    [(8, 20), (6, 20)],  # 9
    []  # extra
]

N2 = 6
M2 = 6
C2 = [1, 2, 6]
G2 = [
    [],  # extra
    [(3, 10)],  # 1
    [(3, 40), (4, 100)],  # 2
    [(4, 80), (1, 10), (2, 40)],  # 3
    [(5, 50), (3, 80), (2, 100)],  # 4
    [(6, 20), (4, 50)],  # 5
    [(5, 20)],  # 6
    []  # extra
]

N3 = 3
M3 = 2
C3 = [1, 3]
G3 = [
    [],
    [(2, 50)],
    [(1, 50), (3, 1000000000)],
    [(2, 1000000000)],
    []
]
