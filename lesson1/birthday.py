import datetime


class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        date = datetime.datetime.now().year
        age = date - year
        return cls(name, age)


    def display(self):
        return f"Это {self.name}, ему {self.age}"


person_1 = Person.fromBirthYear("Николай", 1975)
print(person_1.display())

person_2 = Person('Николай', 25)
print(person_2.display())