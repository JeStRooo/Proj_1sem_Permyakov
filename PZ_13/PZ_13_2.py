"""
Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
последних сроках и столбцах матрицы Matr2 произвольного размера.
"""

from random import randint

len_m = int(input('Введите размер матрицы: '))

matrix = [[randint(-100, 100) for i in range(len_m)] for j in range(len_m)] #создание матрицы
print("Изначальная матрица: ")
for i in matrix:  # вывод матрицы
   print(*i, sep='\t' * 2)
print("\n")


col_m1 = len_m - 1
m2 = len_m - len_m
for item in range(0, len(matrix)):
    matrix[item][col_m1] = matrix[item][col_m1] * 0
    matrix[item][m2] = matrix[item][m2] * 0
matrix[len_m - 1] = list(map(lambda x: x * 0, matrix[len_m - 1]))
matrix[m2] = list(map(lambda x: x * 0, matrix[m2]))
for i in matrix:  # вывод матрицы
   print(*i, sep='\t' * 2)