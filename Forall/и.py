import random

# Генерация списков
list1 = [random.randint(78, 85) for _ in range(100)]  # Список значений от 78 до 85
list2 = [random.randint(70, 85) for _ in range(100)]  # Список значений от 70 до 85

# Вычисление средних арифметических значений
average1 = sum(list1) / len(list1)
average2 = sum(list2) / len(list2)

# Печать результатов
print(f'Список 1 (78-85): {list1}')
print(f'Среднее арифметическое для списка 1: {average1:.2f}')

print(f'\nСписок 2 (70-85): {list2}')
print(f'Среднее арифметическое для списка 2: {average2:.2f}')
