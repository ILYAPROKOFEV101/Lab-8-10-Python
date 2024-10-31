class Transport:
    def __init__(self, transport_type, capacity):
        self.transport_type = transport_type  # Тип транспорта
        self.capacity = capacity  # Грузоподъёмность

    def set_transport_type(self, transport_type):
        self.transport_type = transport_type

    def get_capacity(self):
        return self.capacity


class Car(Transport):
    def __init__(self, transport_type, capacity):
        super().__init__(transport_type, capacity)
        self.load_weight = 0  # Изначально вес груза равен 0

    def set_load_weight(self, weight):
        if weight <= self.capacity:
            self.load_weight = weight
            print(f"Вес груза установлен: {self.load_weight} кг")
        else:
            print(f"Ошибка: Вес груза не может превышать предельную грузоподъёмность: {self.capacity} кг")

    def increase_load_weight(self, increment=20):
        if self.load_weight + increment > self.capacity:
            print(f"Ошибка: Превышение грузоподъёмности! Текущий вес: {self.load_weight} кг, "
                  f"не хватает {self.load_weight + increment - self.capacity} кг.")
            return False  # Возвращаем False, если превышение
        else:
            self.load_weight += increment
            print(f"Текущий вес груза: {self.load_weight} кг")
            return True  # Возвращаем True, если увеличение успешно


# Пример использования
if __name__ == "__main__":
    # Задаём тип транспорта и грузоподъёмность
    car = Car("Автомобиль", 200)  # Автомобиль с грузоподъёмностью 100 кг

    # Показываем грузоподъёмность
    print(f"Грузоподъёмность автомобиля: {car.get_capacity()} кг")

    # Устанавливаем начальный вес груза
    car.set_load_weight(80)  # Установим груз весом 80 кг

    # Увеличиваем вес груза по 20 кг, пока не превысит грузоподъёмность
    while True:
        # Попытка увеличить вес
        if not car.increase_load_weight(10):
            break  # Прерываем цикл, если произошло превышение
