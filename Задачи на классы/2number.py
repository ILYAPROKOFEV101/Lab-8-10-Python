import math


import math

import math

import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)  # Преобразуем радиус в число

    # Метод для вычисления периметра (длины окружности)
    def get_perimeter(self):
        return 2 * math.pi * self.radius

    # Метод для вычисления площади круга
    def get_area(self):
        return math.pi * self.radius ** 2

    # Метод для получения подписи
    def get_caption(self):
        return f"Круг с радиусом {self.radius}"


# Функция для получения радиуса с обработкой исключений
def get_radius(prompt):
    while True:
        try:
            radius = float(input(prompt))
            return radius
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число для радиуса.")


# Запрос у пользователя радиусов для двух кругов с обработкой исключений
first = get_radius("Введите радиус первого круга: ")
second = get_radius("Введите радиус второго круга: ")

# Создаем два объекта класса Circle
circle1 = Circle(first)
circle2 = Circle(second)

# Выводим площадь для первого объекта
print(f"{circle1.get_caption()} - Площадь: {circle1.get_area()}")

# Выводим периметр и площадь для второго объекта
print(f"{circle2.get_caption()} - Периметр: {circle2.get_perimeter()}")
print(f"{circle2.get_caption()} - Площадь: {circle2.get_area()}")
