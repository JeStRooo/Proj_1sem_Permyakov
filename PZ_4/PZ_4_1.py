#Дано вещественное число X и целое число N (>0).
#Найти значение выражеия X - X^3/(3!) + X^5/(5!) - ... + (-1)^N - X^2-N+1/((2-N+1)!) (N! = 12 ...N).
#Полученное число является приближенным значением функции sin в точке X.
x = float(input('Введите первое число: ')) #Ввод наших значений
n = int(input('Введите второе число: ')) + 2

i = 1
answer = 0
plusMinus = True #Перменная для чередования + и -.У которой изначальное значение равное True. То есть '+'
def factorial(num, res = 1, f = 1): #Функция вычисления факториала
    while f != num + 1:
        res *= f
        f += 1
    return res

while i != n:
    if plusMinus == True: #Сначала мы производим сумму
        answer = answer + (x ** i) / factorial(i)
        i += 2
        plusMinus = False
        # После чего мы заменяем значение нашей переменной на False. То есть '-'
    else:
        answer = answer - (x ** i) / factorial(i)
        i += 2
        plusMinus = True

print(answer)
