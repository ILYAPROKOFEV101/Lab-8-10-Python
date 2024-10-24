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


# Демонстрация работы с объектами

# Создаём первый автомобиль с грузоподъёмностью 1000 кг
car1 = Car(1000)

# Устанавливаем вес груза в 500 кг
car1.set_cargo_weight(500)

# Пытаемся увеличить вес на 10 кг (в пределах нормы)
car1.increase_cargo_weight()

# Пытаемся увеличить вес так, чтобы превысить грузоподъёмность
car1.increase_cargo_weight(600)

# Создаём второй автомобиль с грузоподъёмностью 1500 кг
car2 = Car(1500)

# Устанавливаем вес груза в 1600 кг (превышает грузоподъёмность)
car2.set_cargo_weight(1600)

# Устанавливаем вес груза в 1000 кг и увеличиваем его до предела
car2.set_cargo_weight(1000)
car2.increase_cargo_weight(500)  # Увеличиваем на 500 кг
