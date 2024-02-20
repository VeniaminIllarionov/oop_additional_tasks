"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import datetime


class Timer:
    def __enter__(self):
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        self.elapsed_time = self.end - self.start


with Timer() as timer:
    [int(n) for n in range(100)]
print("Execution time:", timer.elapsed_time)
