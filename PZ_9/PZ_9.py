#Организовать словарь avto, содержащий 3 ключа(марки авто) и списки из трёх моделей в качестве значений.
#Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.

avto = {
    'BMW': ['BMW MS', 'BMW 32', 'BMW X6'],
    'Lamborgini': ['Urus', 'Huracan', 'Aventador'],
    'Koenigsegg': ['Koenigsegg Agera', 'Koenigsegg SX', 'Koenigsegg Regera']
}

for i in avto:
    print(avto[i][1])