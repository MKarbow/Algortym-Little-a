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
        [Inf, 5, 4, 6, 6],
        [8, Inf, 5, 3, 4],
        [4, 3, Inf, 3, 1],
        [8, 2, 5, Inf, 6],
        [2, 2, 7, 0, Inf]
    ]

    matrix = [
        [Inf, 1, 5, 2, 2, 7, 5],
        [3, Inf, 2, 6, 1, 9, 5],
        [1, 2, Inf, 2, 9, 5, 8],
        [4, 7, 3, Inf, 4, 5, 2],
        [5, 2, 7, 8, Inf, 9, 1],
        [8, 6, 4, 3, 2, Inf, 7],
        [5, 9, 6, 4, 2, 8, Inf]
    ]

    # Lista podproblemów PP: każdy podproblem to obiekt klasy PP
    PP_list = []

    low_limit = krok1.reduce(matrix)

    idx = 0

    # dodaj problem główny do listy
    PP_list.append(krok3.PP(idx, matrix, low_limit, [], False))

    idx += 1

    v_star = Inf

    while PP_list:

        # pomocnicza lista do znalezienia niezamkniętych PP
        filter = [elem for elem in PP_list if elem.kz is False]
        # element o najniższym lb i niezamknięty
        min_PP = min(filter, key=lambda x: x.lb)
        PP_list.remove(min_PP)
        # krok 2:
        i, j = krok2.get_edge_max_opt_exl_cost(min_PP.reduced_matrix)
        # krok 3:
        lb1, lb2, PP1, PP2 = krok3.step_3(min_PP, i, j)

        # krok 4:
        kz1, v1, update1 = krok4.kz(lb1, PP1, min_PP.partial_solution, v_star)
        if update1:
            v_star = v1
        kz2, v2, update2 = krok4.kz(lb2, PP2, min_PP.partial_solution, v_star)
        if update2:
            v_star = v2

        # dodanie do ścieżki pierwszego podproblemu (i, j)
        updated_partial_solution = deepcopy(min_PP.partial_solution)
        updated_partial_solution.append((i, j))

        PP_list.append(krok3.PP(idx, PP1, lb1, updated_partial_solution, kz1))
        idx += 1
        PP_list.append(krok3.PP(idx, PP2, lb2, min_PP.partial_solution, kz2))
        idx += 1

        # jeśli wszystkie podproblemy zamknięte (True) - koniec
        state_of_openness = [elem.kz for elem in PP_list]
        if all(state_of_openness):
            break

    solution = [elem for elem in PP_list if len(elem.partial_solution) == len(matrix)]
    print(PP_list)
    print('\n\n\n\nROZWIĄZANIE: ')
    print(solution)
    # ścieżki na podstawie rozwiazań:
    for elem in solution:
        # arbitralne dodanie pierwszych 2 wierzchołków
        # następnie szukana jest krawędź zaczynająca się dotychczasowym końcem ścieżki
        path = []
        path.append(elem.partial_solution[0][0])
        path.append(elem.partial_solution[0][1])
        while len(path) != len(matrix) + 1:
            for el in elem.partial_solution:
                if el[0] == path[-1]:
                    path.append(el[1])
        print(path)


if __name__ == '__main__':
    main()
