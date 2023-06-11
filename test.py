import unittest
from krok1 import *
from krok2 import *
from krok3 import *
from krok4 import *
from all_steps_ import *


class LittleAlgorithmTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LittleAlgorithmTest, self).__init__(*args, **kwargs)
        self.matrix = [
            [Inf, 5, 4, 6, 6],
            [8, Inf, 5, 3, 4],
            [4, 3, Inf, 3, 1],
            [8, 2, 5, Inf, 6],
            [2, 2, 7, 0, Inf]
        ]
        self.matrix_reduced = [
            [Inf, 1, 0, 2, 2],
            [3, Inf, 2, 0, 1],
            [1, 2, Inf, 2, 0],
            [4, 0, 3, Inf, 4],
            [0, 2, 7, 0, Inf]
        ]
        self.lb = 12
        self.i_star = 3
        self.j_star = 1
        self.lb1 = 13
        self.lb2 = 16
        self.pp1 = [
            [Inf, Inf, 0, 2, 2],
            [2, Inf, 1, Inf, 0],
            [1, Inf, Inf, 2, 0],
            [Inf, Inf, Inf, Inf, Inf],
            [0, Inf, 7, 0, Inf]
        ]
        self.pp2 = [
            [Inf, 0, 0, 2, 2],
            [3, Inf, 2, 0, 1],
            [1, 1, Inf, 2, 0],
            [1, Inf, 0, Inf, 1],
            [0, 1, 7, 0, Inf]
        ]

    def test_step1(self):

        lb = reduce(self.matrix)
        self.assertEqual(self.matrix, self.matrix_reduced)
        self.assertEqual(self.lb, lb)

        reduce(matrix1)
        reduce(matrix2)
        reduce(matrix3)
        reduce(matrix4)
        reduce(matrix5)

    def test_step2(self):
        i_star, j_star = get_edge_max_opt_exl_cost(self.matrix_reduced)
        self.assertEqual((self.i_star, self.j_star), (i_star, j_star))

        reduce(matrix1)
        get_edge_max_opt_exl_cost(matrix1)
        reduce(matrix2)
        get_edge_max_opt_exl_cost(matrix2)
        reduce(matrix3)
        get_edge_max_opt_exl_cost(matrix3)
        reduce(matrix4)
        get_edge_max_opt_exl_cost(matrix4)
        reduce(matrix5)
        get_edge_max_opt_exl_cost(matrix5)

    def test_step3(self):
        pp = PP(0, self.matrix_reduced, self.lb, [], False)
        lb1, lb2, pp1, pp2 = step_3(pp, self.i_star, self.j_star)
        self.assertEqual((lb1, lb2), (self.lb1, self.lb2))
        self.assertEqual(pp1, self.pp1)
        self.assertEqual(pp2, self.pp2)

        lb1 = reduce(matrix1)
        i1, j1 = get_edge_max_opt_exl_cost(matrix1)
        pp1 = PP(1, matrix1, lb1, [], False)
        step_3(pp1, i1, j1)
        lb2 = reduce(matrix2)
        i2, j2 = get_edge_max_opt_exl_cost(matrix2)
        pp2 = PP(2, matrix2, lb2, [], False)
        step_3(pp2, i2, j2)
        lb3 = reduce(matrix3)
        i3, j3 = get_edge_max_opt_exl_cost(matrix3)
        pp3 = PP(3, matrix3, lb3, [], False)
        step_3(pp3, i3, j3)
        lb4 = reduce(matrix4)
        i4, j4 = get_edge_max_opt_exl_cost(matrix4)
        pp4 = PP(4, matrix4, lb4, [], False)
        step_3(pp4, i4, j4)
        lb5 = reduce(matrix5)
        i5, j5 = get_edge_max_opt_exl_cost(matrix5)
        pp5 = PP(2, matrix5, lb5, [], False)
        step_3(pp5, i5, j5)

    def test_step4(self):
        pass

    def test_step5(self):
        pass


if __name__ == '__main__':
    unittest.main()
