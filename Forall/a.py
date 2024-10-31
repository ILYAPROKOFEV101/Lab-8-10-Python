import random

# Генерируем значениеN случайным образом из диапазона от 60 до 100
valueN = random.randint(60, 100)

# Генерируем Значение1 и Значение2
# Значение1 будет фиксировано в диапазоне от 70 до 85
# Значение2 будет фиксировано в диапазоне от 70 до 77 (так как должно быть меньше на 8 баллов)
value1 = random.randint(70, 85)
value2 = value1 - random.randint(8, 15)  # Значение2 должно быть на 8-15 меньше, чтобы гарантировать разницу не менее 8

# Проверяем условие, что значение2 находится в правильном диапазоне
if value2 < 70:
    value2 = value1 - 8  # Если значение2 меньше 70, устанавливаем его на 8 меньше, чтобы соответствовать требованиям

print(f'ЗначениеN: {valueN}')
print(f'Значение1: {value1}')
print(f'Значение2: {value2}')