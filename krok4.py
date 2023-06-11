# kryteria zamykania podproblemów


def kz(lb, v_star=float('inf')):

    # kz1
    if lb == float('inf'):
        return True, v_star  # podproblem zamknięty

    # kz2
    if lb >= v_star:
        return True, v_star  # podproblem zamknięty

    # kz3
    if lb < v_star:
        v_star = lb
        return False, v_star

    return False, v_star


'''
każdy problem to: (macierz, lb, current_path)

for problem in list_of_problems: 
    closed, v_star = kz(problem[0], problem[1], problem[2], v_star)
    if closed:
        list_of_problems.remove(problem)
if not list_of_problems:
    STOP
    rozwiązanie = v_star
else:
    continue (krok2.)
'''

"""
WSTĘPNY SCHEMAT FUNCKJI
def TSP(matrix, v_star=inf):
    LP = [(matrix, 0, [])]
    ->krok1
    while True:
        ->krok2
        ->krok3
            tutaj do LP są dołączane nowe problemy
        ->krok4 czyli mój wcześniejszy kod (ale tylko dla nowych podproblemów?)
            jeśli lista problemów lub podproblemów pusta:
                break
            else:
                continue
    return v_star, path (z tego ostatniego podproblemu?)
"""