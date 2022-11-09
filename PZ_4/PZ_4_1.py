#Дано вещественное число X и целое число N (>0).
#Найти значение выражеия X - X^3/(3!) + X^5/(5!) - ... + (-1)^N - X^2-N+1/((2-N+1)!) (N! = 12 ...N).
#Полученное число является приближенным значением функции sin в точке X.
import math #Импортируем библиотеку, чтобы не было ошибки
# OverflowError: целое число слишком длинное, для преобразования в вещественное число.

X = input('Введите первое число: ') #Ввод наших значений
N = input('Введите второе число: ')

i = 1
answer = 0
plusMinus = True #Перменная для чередования + и -.У которой изначальное значение равное True. То есть '+'

def factorial(num, res = 1, f = 1): #Функция вычисления факториала
    while f != num + 1:
        res *= f
        f += 1
    return res

while (type(X) != float) & (type(N) != int): #Запускаем цикл - обработчик ошибок ValueError
    try: #Перобразовываем наши введённые значения
        X = float(X)
        N = int(N) + 2
    except ValueError:
        print('Вы ввели неверное значение!')
        X = input('Введите первое число: ')
        N = input('Введите второе число: ')
while i != N:
     if plusMinus == True: #Сначала мы производим сумму
        answer = answer + (X ** i) / math.factorial(factorial(i)) #Производим наше решение задачи
        i += 2
        plusMinus = False
        #После чего мы заменяем значение нашей переменной на False. То есть '-'
     else:
        answer = answer - (X ** i) / math.factorial(factorial(i))
        i += 2
        plusMinus = True
print(answer)