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


# Создаем два объекта класса Circle
first = float(input("Введи радиус первого круга: "))
second = float(input("Введи радиус второго круга: "))

circle1 = Circle(first)
circle2 = Circle(second)

# Выводим площадь для первого объекта
print(f"Площадь круга с радиусом {circle1.radius}: {circle1.get_area()}")

# Выводим периметр и площадь для второго объекта
print(f"Периметр круга с радиусом {circle2.radius}: {circle2.get_perimeter()}")
print(f"Площадь круга с радиусом {circle2.radius}: {circle2.get_area()}")
