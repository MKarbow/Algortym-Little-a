from typing import List, Tuple

Inf = float('inf')


def get_edge_max_opt_exl_cost(mtx: List[List[int]]) -> Tuple[int, int]:
    """
    Funkcja zwracjąca indeksy krawędzi o maksymalnym optymalnym koszcie wyłączenia
    do algorytmu Little'a do rozwiązania problemu TSP
    :param mtx: (List[List[int]]) : Macierz kosztów przejścia
    :return: (Tuple[int, int]) : Krotka indeksów i*, j*
    """
    i_star = -1  # indeks i* wynikowej krawędzi
    j_star = -1  # indeks j* wynikowej krawędzi
    d_max = -1  # największy koszt wyłączenia odcinka
    for i, row in enumerate(mtx):
        for j, val in enumerate(row):
            if val == 0:  # dla każdej wartości równej 0
                min_row = Inf
                min_col = Inf
                for i_, row_ in enumerate(mtx):
                    for j_, val_ in enumerate(row_):
                        if i_ != i or j_ != j:  # pomija się indeksy elementu zerowego
                            if i_ == i:
                                if val_ < min_row:
                                    min_row = val_
                            if j_ == j:
                                if val_ < min_col:
                                    min_col = val_
                d = min_row + min_col  # wyznacza się koszt
                if d > d_max:  # aktualizuje się największy koszt wyłączenia i indeksy krawędzi
                    d_max = d
                    i_star = i
                    j_star = j
    return i_star, j_star


"""
test_mtx = [[Inf, 1, 0, 2, 2],
            [3, Inf, 2, 0, 1],
            [1, 2, Inf, 2, 0],
            [4, 0, 3, Inf, 4],
            [0, 2, 7, 0, Inf]]

i_, j_ = get_edge_max_opt_exl_cost(test_mtx)
print(i_, j_)
"""
