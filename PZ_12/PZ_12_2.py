'''
Составить генератор (yield), который преобразует все буквенные символы в заглавные.
'''

def str_to_lower(crs: str): #Создаём генератор
    for i in crs:
        yield i.upper()

print(''.join(str_to_lower('big')))