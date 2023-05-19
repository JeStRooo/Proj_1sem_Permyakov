"""
Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать".
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def purr(self):
        print(f"{self.name} is purring")

dog = Dog('Anton')
cat = Cat('Rozie')

dog.breathe()
cat.breathe()