import numpy as np

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


def step_3(i, j, P, low_limit):
    PP_1 = P
    PP_2 = P
    for m in range(len(P)):
        PP_1[m][j] = np.inf
    for n in range(len(P[0])):
        PP_1[i][n] = np.inf

    low_limit_1 = low_limit + reduce(PP_1)

    PP_2[i][j] = np.inf
    low_limit_2 = low_limit + reduce(PP_2)

    return low_limit_1, low_limit_2, PP_1, PP_2


class PP:
    def __init__(self, id, reduced_matrix, lb, partial_solution, kz):
        self.id = id
        self.reduced_matrix = reduced_matrix
        self.lb = lb
        self.partial_solution = partial_solution
        self.kz = kz


def main():
    #test
    step_3(2, 3, [[np.inf, 3, 4, 5], [3, np.inf, 4, 4], [0, 2, np.inf, 3], [2, 2, 1, np.inf]])



if __name__ == '__main__':
    main()




