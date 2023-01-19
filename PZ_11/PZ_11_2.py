#Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего регистра на нижний.

w = 0
for i in open('text19.txt', encoding='UTF-8'):
    print(i, end='')
    for j in i:
        if j.isalpha():
            w += 1
print(end='\n')
print('Количество букв: ', w, end='\n')

f1 = open('text19.txt', encoding='UTF-8')
l = f1.readlines()
new_l = [x.lower() for x in l]
f1.close()
f2 = open('text19-2.txt', 'w')
f2.writelines(new_l)
f2.close()

