'''
В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.
'''

list = [1, 2, 5, 7, 7, 3, 4, 5, 6]

list_one_thrid = list[:int(len(list) / 3)]
sum_list = sum(list_one_thrid)
lst_avg = sum_list / len(list_one_thrid)
print('Среднее арифметическое: ', lst_avg)