import numpy as np
from copy import deepcopy
from krok2 import get_edge_max_opt_exl_cost
from krok1 import reduce

Inf = float('inf')

# znajdź w macierzy miejsca, które nie są infami czyli potencjalne do zakazania (mogą być tam cykle)
def find_potential_errors(matrix):
    errors = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != Inf:
                errors.append((i, j))
    return errors

# następne 2 w pętli for, dla każdego z errors zwróconego wcześniej
# dodaj ten odcinek do obecnej ścieżki
def path_to_be_checked(path, ij):
    new_path = deepcopy(path)
    new_path.append(ij)
    return new_path

# i sprawdź czy z tym odcinkiem będzie w ścieżce cykl
# (jesli się tak okaże - trzeba tam zakazać tego przejścia error w macierzy)
def find_cycle(path):
    sorted_path = [path[0]]
    cycle = False
    new_cycle = False
    # dopóki nie powstanie ułożona ścieżka
    while len(sorted_path) != len(path):
        if cycle:
            break
        end = sorted_path[-1][1]  # koniec aktualny
        added = False
        for elem in path:  # znajdź taki odcinek, żeby zaczynał się tym endem
            if elem[0] == end:
                # spr czy ten odcinek jest już dodany
                if elem in sorted_path and not new_cycle:
                    cycle = True  # znalezniono cykl
                    new_cycle = False
                    break
                # jeśli nie, to dodaj go
                else:
                    sorted_path.append(elem)
                    added = True
                    break
        # jeśli nic nie zostało dodane i nie ma znaleziono cyklu
        if not added and not cycle:
            # dodaj pierwszy niedodany odcinek
            for elem in path:
                if elem not in sorted_path:
                    sorted_path.append(elem)
                    new_cycle = True
                    break
    one_cycle = True
    for i in range(len(sorted_path)-1):
        if sorted_path[i][1] != sorted_path[i+1][0]:
            one_cycle = False
            break
    if one_cycle and sorted_path[0][0] == sorted_path[-1][1]:
        cycle = True
    return cycle

def step_3(min_PP, i, j):

    PP_1 = deepcopy(min_PP.reduced_matrix)
    PP_2 = deepcopy(min_PP.reduced_matrix)

    # zabroń wiersza i kolumny dla (i, j)
    for m in range(len(min_PP.reduced_matrix)):
        PP_1[m][j] = np.inf
    for n in range(len(min_PP.reduced_matrix[0])):
        PP_1[i][n] = np.inf

    # znajdź potencjalne cykle (opisy w funkcjach)
    errs = find_potential_errors(PP_1)
    for ij in errs:
        new_path = path_to_be_checked(min_PP.partial_solution, ij)
        cycle = find_cycle(new_path)
        if cycle:
            PP_1[ij[0]][ij[1]] = Inf

    PP_1[j][i] = Inf

    # nowy LB
    low_limit_1 = min_PP.lb + reduce(PP_1)

    # zakaz (i,j) w macierzy
    PP_2[i][j] = np.inf

    #nowy LB
    low_limit_2 = min_PP.lb + reduce(PP_2)

    return low_limit_1, low_limit_2, PP_1, PP_2

#Struktura przechowująca podproblemy
class PP:

    def __init__(self, id, reduced_matrix, lb, partial_solution, kz):
        self.id = id
        self.reduced_matrix = reduced_matrix
        self.lb = lb
        self.partial_solution = partial_solution
        self.kz = kz

    def __repr__(self):
        return '-------\nID: {} \nMacierz: {}\nLB: {}\nCzęściowe rozwiązanie: {}\nKZ:{}\n--------'.format(self.id, self.reduced_matrix, self.lb, self.partial_solution, self.kz)

