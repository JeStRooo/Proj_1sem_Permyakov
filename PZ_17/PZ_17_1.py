class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return (sum(self.grades) / len(self.grades)) >= 4.5

student_1 = Student('Ivan', 'Medvedev', [4, 4, 5])

print(student_1.average_grade())
print(student_1.is_excellent())