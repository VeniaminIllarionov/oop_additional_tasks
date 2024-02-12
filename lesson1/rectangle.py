class Rectangle:
    length: float
    width: float

    def __init__(self, length, width):
        self.width = width
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.length * self.width

    def display(self):
        return (f"Длина равна {self.length}\n"
                f"Ширина равна {self.width}\n"
                f"Площадь равна {self.area()}\n"
                f"Периметр равен {self.perimeter()}")


Rectangle_ = Rectangle(7.1, 8)
print(Rectangle_.display())