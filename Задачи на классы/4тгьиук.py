class Transport:
    def __init__(self, transport_type, capacity):
        self.transport_type = transport_type
        self.capacity = capacity  # Грузоподъёмность в килограммах

    # Метод для задания типа транспорта
    def set_transport_type(self, transport_type):
        self.transport_type = transport_type

    # Метод для задания грузоподъёмности
    def set_capacity(self, capacity):
        self.capacity = capacity

    # Метод для получения грузоподъёмности
    def get_capacity(self):
        return self.capacity


class Car(Transport):
    def __init__(self, capacity, cargo_weight=0):
        super().__init__('Автомобиль', capacity)
        self.cargo_weight = cargo_weight  # Вес груза

    # Метод для задания веса груза (не должен превышать грузоподъёмность)
    def set_cargo_weight(self, weight):
        if weight <= self.capacity:
            self.cargo_weight = weight
            print(f"Вес груза установлен: {self.cargo_weight} кг")
        else:
            print(f"Ошибка: вес груза превышает грузоподъёмность {self.capacity} кг")

    # Метод для увеличения веса груза с шагом 10 кг
    def increase_cargo_weight(self, increment=10):
        if self.cargo_weight + increment <= self.capacity:
            self.cargo_weight += increment
            print(f"Текущий вес груза: {self.cargo_weight} кг")
        else:
            print(f"Ошибка: превышена грузоподъёмность {self.capacity} кг")


# Функция для ввода данных о грузоподъёмности
def get_capacity():
    while True:
        try:
            capacity = float(input("Введите грузоподъёмность (в кг): "))
            if capacity <= 0:
                print("Ошибка: грузоподъёмность должна быть положительным числом.")
                continue
            return capacity
        except ValueError:
            print("Ошибка: введите корректное число.")


# Функция для ввода данных о весе груза
def get_cargo_weight():
    while True:
        try:
            weight = float(input("Введите вес груза (в кг): "))
            if weight < 0:
                print("Ошибка: вес груза не может быть отрицательным.")
                continue
            return weight
        except ValueError:
            print("Ошибка: введите корректное число.")


# Демонстрация работы с объектами

# Создаем первый автомобиль
print("Создание первого автомобиля:")
capacity1 = get_capacity()
car1 = Car(capacity1)

# Устанавливаем вес груза
cargo_weight1 = get_cargo_weight()
car1.set_cargo_weight(cargo_weight1)

# Пытаемся увеличить вес на 10 кг (в пределах нормы)
car1.increase_cargo_weight(10)

# Пытаемся увеличить вес так, чтобы превысить грузоподъёмность
car1.increase_cargo_weight(600)  # Увеличение на 600 кг, ожидается ошибка

# Создаем второй автомобиль
print("\nСоздание второго автомобиля:")
capacity2 = get_capacity()
car2 = Car(capacity2)

# Устанавливаем вес груза
cargo_weight2 = get_cargo_weight()
car2.set_cargo_weight(cargo_weight2)

# Устанавливаем вес груза в 1000 кг и увеличиваем его до предела
car2.set_cargo_weight(1000)
car2.increase_cargo_weight(500)  # Увеличиваем на 500 кг
