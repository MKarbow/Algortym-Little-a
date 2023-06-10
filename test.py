import unittest
from krok1 import *
from krok2 import *
from krok3 import *


class LittleAlgorithmTest(unittest.TestCase):
    def test_step1(self):
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

        lb = reduce(matrix0)
        self.assertEqual(matrix0, ex_res)
        self.assertEqual(lb, 12)

        reduce(matrix1)
        reduce(matrix2)
        reduce(matrix3)
        reduce(matrix4)
        reduce(matrix5)

    def test_step2(self):
        matrix0 = [
            [Inf, 1, 0, 2, 2],
            [3, Inf, 2, 0, 1],
            [1, 2, Inf, 2, 0],
            [4, 0, 3, Inf, 4],
            [0, 2, 7, 0, Inf]
        ]

        i_star, j_star = get_edge_max_opt_exl_cost(matrix0)
        self.assertEqual((i_star, j_star), (3, 1))

        get_edge_max_opt_exl_cost(matrix1)
        get_edge_max_opt_exl_cost(matrix2)
        get_edge_max_opt_exl_cost(matrix3)
        get_edge_max_opt_exl_cost(matrix4)
        get_edge_max_opt_exl_cost(matrix5)

    def test_step3(self):
        pass

    def test_step4(self):
        pass

    def test_step5(self):
        pass


if __name__ == '__main__':
    unittest.main()
