#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных
# и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы до n-1 умножены на элемент n:

list = ['100 -15 45']
f19 = open('data_19.txt', 'w')
f19.writelines(list)
f19.close()

f20 = open('data_20.txt', 'w')
f20.write('Исходные данные: ')
f20.write('\n')
f20.writelines(list)
f20.close()

f19 = open('data_19.txt')
k = f19.read()
k = k.split()
for i in range(len(k)):
 k[i] = int(k[i])
f19.close()

f19 = open('data_19.txt')

t = 0
sum = 0
mult = 1

for i in range(len(k)):
 sum += k[i]
 if k[i] < 0:
    t += 1

for i in range(len(k)):
 mult *= k[i]
 if k[i] < 0:
    t += 1

f20 = open('data_20.txt', 'a')
f20.write('\n')
print('Количество элементов: ', len(k), '\n', 'Сумма элементов: ', sum, '\n', 'Произведение: ', mult, file=f20)
f20.close()