
import numpy as np
import copy

inf = float('inf')

def matrix_reduction(original_matrix: np.ndarray) -> (np.ndarray, np.ndarray, int):

    lb = 0
    buffor_matrix = copy.deepcopy(original_matrix)

    for row in buffor_matrix:
        if not np.any(row == 0):
            minimum = np.min(row)
            lb += minimum
            row -= minimum

    buffor_matrix = buffor_matrix.T

    for row in buffor_matrix:
        if not np.any(row == 0):
            minimum = np.min(row)
            lb += minimum
            row -= minimum

    buffor_matrix = buffor_matrix.T

    return buffor_matrix, lb

# Macierze testowe

matrix1 = [
    [inf, 1, 5, 2, 2, 7],
    [3, inf, 2, 6, 1, 4],
    [1, 2, inf, 2, 9, 5],
    [4, 7, 3, inf, 4, 5],
    [5, 2, 7, 8, inf, 9],
    [8, 6, 4, 3, 2, inf]
           ]

matrix2 = [
    [inf, 1, 5, 2, 2, 7, 5],
    [3, inf, 2, 6, 1, 9, 5],
    [1, 2, inf, 2, 9, 5, 8],
    [4, 7, 3, inf, 4, 5, 2],
    [5, 2, 7, 8, inf, 9, 1],
    [8, 6, 4, 3, 2, inf, 7],
    [5, 9, 6, 4, 2, 8, inf]
]

matrix3 = [
    [inf, 1, 5, 2, 2, 7, 5, 3],
    [3, inf, 2, 6, 1, 9, 5, 2],
    [1, 2, inf, 2, 9, 5, 8, 7],
    [4, 7, 3, inf, 4, 5, 2, 6],
    [5, 2, 7, 8, inf, 9, 1, 4],
    [8, 6, 4, 3, 2, inf, 7, 9],
    [5, 9, 6, 4, 2, 8, inf, 3],
    [3, 1, 7, 9, 5, 6, 4, inf]
]

matrix4 = [
    [inf, 1, 5, 2, 2, 7, 5, 3, 4, 6],
    [3, inf, 2, 6, 1, 9, 5, 2, 8, 4],
    [1, 2, inf, 2, 9, 5, 8, 7, 3, 1],
    [4, 7, 3, inf, 4, 5, 2, 6, 9, 7],
    [5, 2, 7, 8, inf, 9, 1, 4, 6, 5],
    [8, 6, 4, 3, 2, inf, 7, 9, 1, 3],
    [5, 9, 6, 4, 2, 8, inf, 3, 7, 2],
    [3, 1, 7, 9, 5, 6, 4, inf, 2, 1],
    [4, 8, 2, 5, 6, 1, 3, 7, inf, 4],
    [2, 6, 9, 7, 3, 1, 5, 4, 8, inf]
]

matrix5 = [
    [inf, 1, 5, 2, 2, 7, 5, 3, 4, 6, 7, 9],
    [3, inf, 2, 6, 1, 9, 5, 2, 8, 4, 3, 1],
    [1, 2, inf, 2, 9, 5, 8, 7, 3, 1, 6, 2],
    [4, 7, 3, inf, 4, 5, 2, 6, 9, 7, 4, 8],
    [5, 2, 7, 8, inf, 9, 1, 4, 6, 5, 2, 6],
    [8, 6, 4, 3, 2, inf, 7, 9, 1, 3, 5, 7],
    [5, 9, 6, 4, 2, 8, inf, 3, 7, 2, 9, 5],
    [3, 1, 7, 9, 5, 6, 4, inf, 2, 1, 6, 4],
    [4, 8, 2, 5, 6, 1, 3, 7, inf, 4, 3, 2],
    [2, 6, 9, 7, 3, 1, 5, 4, 8, inf, 7, 9],
    [7, 3, 1, 6, 9, 5, 8, 4, 3, 7, inf, 2],
    [9, 5, 6, 2, 8, 7, 5, 2, 1, 9, 4, inf]
]