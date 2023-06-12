import numpy as np
from copy import deepcopy
from typing import List, Tuple
import krok1
import krok2
import krok3
import krok4

Inf = float('inf')


def main():


    matrix = [
        [Inf, 1, 5, 2, 2, 7, 5],
        [3, Inf, 2, 6, 1, 9, 5],
        [1, 2, Inf, 2, 9, 5, 8],
        [4, 7, 3, Inf, 4, 5, 2],
        [5, 2, 7, 8, Inf, 9, 1],
        [8, 6, 4, 3, 2, Inf, 7],
        [5, 9, 6, 4, 2, 8, Inf]
    ]

    matrix = [
        [Inf, 5, 4, 6, 6],
        [8, Inf, 5, 3, 4],
        [4, 3, Inf, 3, 1],
        [8, 2, 5, Inf, 6],
        [2, 2, 7, 0, Inf]
    ]

    # Lista podproblemów PP: każdy podproblem to obiekt klasy PP
    PP_list = []

    low_limit = krok3.reduce(matrix)

    idx = 0

    PP_list.append(krok3.PP(idx, matrix, low_limit, [], False))

    idx += 1

    v_star = Inf

    while PP_list:

        filter = [elem for elem in PP_list if elem.kz is False]  # pomocnicza lista do znalezienia niezamkniętych PP
        min_PP = min(filter, key=lambda x: x.lb)  # Element o najniższym lb i niezamknięty
        PP_list.remove(min_PP)
        i, j = krok2.get_edge_max_opt_exl_cost(min_PP.reduced_matrix)  # W pierwszym wywołaniu nic nie zmienia, później tak
        # min_PP.reduced_matrix[j][i] = Inf
        lb1, lb2, PP1, PP2 = krok3.step_3(min_PP, i, j)
        print(min_PP.partial_solution)

        # make it make sense
        kz1, v1, update1 = krok4.new_kz(lb1, PP1, min_PP.partial_solution, v_star)
        if update1:
            v_star = v1
        kz2, v2, update2 = krok4.new_kz(lb2, PP2, min_PP.partial_solution, v_star)
        if update2:
            v_star = v2

        updated_partial_solution = deepcopy(min_PP.partial_solution)
        updated_partial_solution.append((i, j))

        PP_list.append(krok3.PP(idx, PP1, lb1, updated_partial_solution, kz1))
        idx += 1
        PP_list.append(krok3.PP(idx, PP2, lb2, min_PP.partial_solution, kz2))
        idx += 1

        # print(PP_list)

        state_of_openness = [elem.kz for elem in PP_list]
        if all(state_of_openness):  # Jeśli wszystkie podproblemy zamknięte - koniec
            break

    print(PP_list)


if __name__ == '__main__':
    main()
