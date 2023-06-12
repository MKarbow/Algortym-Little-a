import numpy as np
from copy import deepcopy
from krok2 import get_edge_max_opt_exl_cost
from krok1 import reduce

Inf = float('inf')

def step_3(min_PP, i, j):

    PP_1 = deepcopy(min_PP.reduced_matrix)
    PP_2 = deepcopy(min_PP.reduced_matrix)

    for m in range(len(min_PP.reduced_matrix)):
        PP_1[m][j] = np.inf
    for n in range(len(min_PP.reduced_matrix[0])):
        PP_1[i][n] = np.inf

    list_of_short_paths = []

    for elem in min_PP.partial_solution:

        appended = False

        if not list_of_short_paths:
            list_of_short_paths.append([elem])
            continue

        idx = 0

        while not appended and idx < len(list_of_short_paths):

            if list_of_short_paths[idx][-1][1] == elem[0]:
                list_of_short_paths[idx].append(elem)
                appended = True
                break

            elif list_of_short_paths[idx][0][0] == elem[1]:
                list_of_short_paths[idx].insert(0, elem)
                appended = True
                break

            idx += 1

        if not appended:
            list_of_short_paths.append([elem])

    if len(list_of_short_paths) > 1:  # możliwość mergowania
        for m in range(len(list_of_short_paths)):
            for n in range(len(list_of_short_paths)):
                if m != n and list_of_short_paths[m][-1][1] == list_of_short_paths[n][0][0]:
                    helper_m = m
                    helper_n = n
        try:
            for el in list_of_short_paths[helper_n]:
                list_of_short_paths[helper_m].append(el)
            list_of_short_paths.remove(list_of_short_paths[helper_n])
        except UnboundLocalError:
            pass

    appended = False
    for elem in list_of_short_paths:
        appended = False
        if elem[-1][1] == i and len(elem) != len(min_PP.reduced_matrix) - 1:  # podcykl
            PP_1[j][elem[0][0]] = np.inf
            appended = True
            break
    if not appended:
        PP_1[j][i] = np.inf

    low_limit_1 = min_PP.lb + reduce(PP_1)

    PP_2[i][j] = np.inf
    low_limit_2 = min_PP.lb + reduce(PP_2)

    return low_limit_1, low_limit_2, PP_1, PP_2


class PP:

    def __init__(self, id, reduced_matrix, lb, partial_solution, kz):
        self.id = id
        self.reduced_matrix = reduced_matrix
        self.lb = lb
        self.partial_solution = partial_solution
        self.kz = kz

    def __repr__(self):
        return '-------\nID: {} \nMacierz: {}\nLB: {}\nCzęściowe rozwiązanie: {}\nKZ:{}\n--------'.format(self.id, self.reduced_matrix, self.lb, self.partial_solution, self.kz)




