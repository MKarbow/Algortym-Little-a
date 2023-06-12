
import numpy as np
import copy

inf = float('inf')
Inf = float('inf')

def reduce(matrix):
    low_limit = 0
    for elem in matrix:  # lists of rows
        min_value = min(elem)
        if min_value != np.inf:
            low_limit += min_value
            for i in range(len(elem)):
                elem[i] = elem[i] - min_value

    for i in range(len(matrix)):  # list of columns
        col = [elem[i] for elem in matrix]
        min_value = min(col)
        if min_value != np.inf:
            low_limit += min_value
            for j in range(len(matrix)):
                matrix[j][i] = matrix[j][i] - min_value

    return low_limit

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

matrix6 = [
    [Inf, 10, 8, 19, 12],
    [10, Inf, 20, 6, 3],
    [8, 20, Inf, 4, 2],
    [19, 6, 4, Inf, 7],
    [12, 3, 2, 7, Inf]
]

matrix7 = [
    [Inf, 3, 4, 2, 7],
    [3, Inf, 4, 6, 3],
    [4, 4, Inf, 5, 8],
    [2, 6, 5, Inf, 6],
    [7, 3, 8, 6, Inf]
]

matrix8 = [
    [Inf, 12, 3, 45, 6],
    [78, Inf, 90, 21, 3],
    [5, 56, Inf, 23, 98],
    [12, 6, 8, Inf, 34],
    [3, 98, 3, 2, Inf]
]