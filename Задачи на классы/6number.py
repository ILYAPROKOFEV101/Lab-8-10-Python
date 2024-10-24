class Sale:

    def __init__(self, product_type, monthly_sales=None):
        self.product_type = product_type  # Вид товара
        self.monthly_sales = monthly_sales or []  # Список сумм продаж за 6 месяцев

    # Метод для задания вида товара
    def set_product_type(self, product_type):
        self.product_type = product_type

    # Метод для задания списка продаж
    def set_monthly_sales(self, sales):
        if len(sales) == 6:
            self.monthly_sales = sales
        else:
            print("Ошибка: нужно указать суммы продаж за 6 месяцев.")

    # Метод для хранения самого удачного месяца
    def best_month(self):
        if not self.monthly_sales:
            print("Ошибка: данные о продажах отсутствуют.")
            return

        # Находим максимальную сумму продаж и индекс этого месяца
        max_sales = max(self.monthly_sales)
        best_month_index = self.monthly_sales.index(max_sales)

        # Список месяцев для удобного отображения
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь']

        # Выводим результат
        print(
            f"Самый удачный месяц для товара '{self.product_type}' — {months[best_month_index]} с продажами на сумму {max_sales} рублей.")


# Демонстрация работы с объектами

# Создаем объект для продаж техники
sale1 = Sale("Техника", [120000, 135000, 110000, 150000, 160000, 140000])

# Определяем самый удачный месяц для техники
sale1.best_month()

# Создаем объект для продаж мебели
sale2 = Sale("Мебель")

# Устанавливаем список продаж для мебели
sale2.set_monthly_sales([50000, 60000, 45000, 70000, 80000, 65000])

# Определяем самый удачный месяц для мебели
sale2.best_month()
