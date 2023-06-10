import numpy as np
from copy import deepcopy
from krok2 import get_edge_max_opt_exl_cost

#Funkcja reduce() z metody węgierskiej, przerobiona dla moich testów
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

    print('Wynik redukcji: ')
    for i in range(len(matrix)):
        print([elem for elem in matrix[i]])
    print('Dolne ograniczenie: ', low_limit, '\n')

    return low_limit


def step_3(min_PP, i, j):

    PP_1 = deepcopy(min_PP.reduced_matrix)
    PP_2 = deepcopy(min_PP.reduced_matrix)

    for m in range(len(min_PP.reduced_matrix)):
        PP_1[m][j] = np.inf
    for n in range(len(min_PP.reduced_matrix[0])):
        PP_1[i][n] = np.inf

    #Podcykl:
    if len(min_PP.partial_solution) < len(min_PP.reduced_matrix) - 1: #Sprawdzamy podcykl jeśli grozi przedwczesne zakończenie
        try:
            p = min_PP.partial_solution[0][0] #pierwszy element rozwiązania
            k = j #ostatni element rozwiązania
            PP_1[k][p] = np.inf
        except IndexError: #w pierwszym etapie partial_solution puste - i tak nie będzie cyklu
            pass

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
        return 'ID: {} \nMacierz: {}\nLB: {}\nCzęściowe rozwiązanie: {}\nKZ:{}'.format(self.id, self.reduced_matrix, self.lb, self.partial_solution, self.kz)


def main():
    matrix = [
        [np.inf, 1, 5, 2, 2, 7, 5, 3],
        [3, np.inf, 2, 6, 1, 9, 5, 2],
        [1, 2, np.inf, 2, 9, 5, 8, 7],
        [4, 7, 3, np.inf, 4, 5, 2, 6],
        [5, 2, 7, 8, np.inf, 9, 1, 4],
        [8, 6, 4, 3, 2, np.inf, 7, 9],
        [5, 9, 6, 4, 2, 8, np.inf, 3],
        [3, 1, 7, 9, 5, 6, 4, np.inf]
    ]

    #Lista podproblemów PP: każdy podproblem to obiekt klasy PP
    PP_list = []

    low_limit = reduce(matrix)

    idx = 0

    PP_list.append(PP(idx, matrix, low_limit, [], False))

    idx += 1

    while PP_list:

        filter = [elem for elem in PP_list if elem.kz is False] #pomocnicza lista do znalezienia niezamkniętych PP
        min_PP = min(filter, key=lambda x: x.lb) #Element o najniższym lb i niezamknięty
        PP_list.remove(min_PP)
        i, j = get_edge_max_opt_exl_cost(min_PP.reduced_matrix)  #W pierwszym wywołaniu nic nie zmienia, później tak
        lb1, lb2, PP1, PP2 = step_3(min_PP, i, j)

        #TODO: Funkcja Marysi sprawdzające kryteria: niech zwraca kz1, kz2
        kz1 = False
        kz2 = False #TYMCZASOWE, do usunięcia kiedy powstanie funkcja Marysi

        updated_partial_solution = deepcopy(min_PP.partial_solution)
        updated_partial_solution.append((i, j))

        PP_list.append(PP(idx, PP1, lb1, updated_partial_solution, kz1))
        idx += 1
        PP_list.append(PP(idx, PP2, lb2, min_PP.partial_solution, kz2))
        idx += 1

        print(PP_list)

        state_of_openness = [elem.kz for elem in PP_list]
        if all(state_of_openness): #Jeśli wszystkie podproblemy zamknięte - koniec
            break




if __name__ == '__main__':
    main()




