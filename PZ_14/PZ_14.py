#Из исходного текстового файла (pazzl.html) выбратьвсе html-коды изображений.
#Посчитать их количество.

import re

file = open('pazzl.html').read()
regExp = re.compile(r"<img.*?>")

print(f"Количество изображений: {len(regExp.findall(file))}")