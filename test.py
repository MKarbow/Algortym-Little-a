import unittest
from krok1 import *
from krok2 import *


class LittleAlgorithmTest(unittest.TestCase):
    def step1_test(self):
        matrix0 = [
            [Inf, 5, 4, 6, 6],
            [8, Inf, 5, 3, 4],
            [4, 3, Inf, 3, 1],
            [8, 2, 5, Inf, 6],
            [2, 2, 7, 0, Inf]
        ]

        ex_res = [
            [Inf, 1, 0, 2, 2],
            [3, Inf, 2, 0, 1],
            [1, 2, Inf, 2, 0],
            [4, 0, 3, Inf, 4],
            [0, 2, 7, 0, Inf]
        ]
        self.assertEqual(matrix_reduction(matrix0), ex_res)
