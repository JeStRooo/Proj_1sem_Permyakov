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