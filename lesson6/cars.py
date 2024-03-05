"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime


class Car:
    brend: str
    model: str
    year: int

    def __init__(self, brend, model, year):
        self.brend = brend
        self.model = model
        if year > datetime.datetime.now().year:
            raise Exception('Эта машина еще не была выпущена')
        else:
            self.year = year


# код для проверки
car = Car('Toyota', 'Corolla', 2022)


car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
