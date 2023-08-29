from random import randint
from typing import List


def fill_matrix(rows: int, cols: int, min_val: int, max_val: int) -> List[List[int]]:
    return [[randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def display_matrix(mass: List[List[int]]) -> None:
    for r in mass:
        print(" ".join(str(element) for element in r))


def transpose_matrix(mass: List[List[int]]) -> List[List[int]]:
    rows = len(mass)
    cols = len(mass[0])

    # Создаем новую матрицу с обращенными размерами и заполняем значениями из исходной матрицы
    transposed_matrix = [[mass[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix


row, column = map(int, input().split())
start, stop = map(int, input().split())
matrix = fill_matrix(row, column, start, stop)
t_matrix = transpose_matrix(matrix)

display_matrix(matrix)
print()
display_matrix(t_matrix)
