"""
    Задание 4
    Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
    Для каждого из трех случаев пользователь задает свои границы диапазона.
    Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
    Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
from random import random

# Генерация случайного целого числа
min_1 = int(input('Введите минимальное число: '))
max_1 = int(input('Введите максимальное число: '))
result = int(random() * (max_1 - min_1 + 1)) + min_1
print(f'Сгенерировано случайное целое число: {result}')

# Генерация случайного вещественного числа
min_1 = float(input('Введите минимальное число: '))
max_1 = float(input('Введите максимальное число: '))
result = random() * (max_1 - min_1) + min_1
print(f'Сгенерировано случайное вещественное число: {round(result, 2)}')

# Генерация случайного символа
min_1 = ord(input('Введите минимальный символ: '))
max_1 = ord(input('Введите максимальный символ: '))
result = int(random() * (max_1 - min_1 + 1)) + min_1
print(f'Сгенерирован случайный символ: {chr(result)}')