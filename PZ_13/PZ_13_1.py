#В матрице найти среднее арифметическое элементов последних двух столбцов.

from random import randint
len_m = int(input('Ввведите размер матрицы: ')) #Ввод размера матрицы
matrix = [[randint(0, 50) for i in range(len_m)] for j in range(len_m)]
print('Изначальная матрица: ')

for i in matrix:
    print(*i, sep='\t' * 2)
arr = []
col_m1 = len_m - 1
col_m2 = len_m - 2
for item in range(0, len(matrix)):
    arr.append(matrix[item][col_m1])
    arr.append(matrix[item][col_m2])
print(f"Наши последние два столбца: {arr}")

sum_of_digits = sum(arr)

print(f"Среднее арифметическое: {sum_of_digits / len(arr)}")