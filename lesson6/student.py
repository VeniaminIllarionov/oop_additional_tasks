"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:
    name: str
    course: int
    grade: list

    def __init__(self, name, course, grade):
        self.name = name
        self.grade = grade
        self.course = course

    def avg_rate(self, *args, **kwargs):
        if self.grade is None:
            raise ZeroDivisionError
        else:
            print(sum(self.grade) / len(self.grade))


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate()  # 4.75

student = Student('Ivan', 'Python', [])
try:
    student.avg_rate()  # 0.0
except ZeroDivisionError:
    print(0.0)
