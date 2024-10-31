class Sale:
    def __init__(self, product_type, monthly_sales=None):
        self.product_type = product_type  # Вид товара
        self.monthly_sales = monthly_sales if monthly_sales is not None else []  # Инициализация списка продаж

    def set_monthly_sales(self, sales):
        """Устанавливаем продажи за 6 месяцев, проверяя длину списка."""
        if len(sales) == 6:
            self.monthly_sales = sales
        else:
            print("Ошибка: нужно указать суммы продаж за 6 месяцев.")

    def best_month(self):
        """Определяем самый удачный месяц."""
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
            f"Самый удачный месяц для товара '{self.product_type}' — {months[best_month_index]} с продажами на сумму {max_sales} рублей."
        )


# Демонстрация работы с объектами

# Создаем объект для продаж техники с начальным списком продаж
sale1 = Sale("Техника", [120000, 135000, 110000, 150000, 160000, 140000])
sale1.best_month()  # Определяем самый удачный месяц для техники

# Создаем объект для продаж мебели без начальных продаж
sale2 = Sale("Мебель")
sale2.set_monthly_sales([50000, 60000, 45000, 70000, 80000, 65000])  # Устанавливаем список продаж
sale2.best_month()  # Определяем самый удачный месяц для мебели
