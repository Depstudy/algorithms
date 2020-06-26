'''
    Задание 4.
    Определить, какое число в массиве встречается чаще всего.
'''
from random import random

try:
    N = int(input('Введите количество элементов: '))
    arr = [int(random() * 5) for i in range(N)]
    val = None  # Наиболее часто встречающееся значение
    quantity = 0    # Количество наиболее часто встречающегося значения


    print(arr)
    for i in arr:
        res = arr.count(i)
        if res > quantity:
            quantity = res
            val = i
    if quantity >= 2:
        print(f'Наиболее частое значение: {val}, количество одинаковых элементов: {quantity}')
    else:
        print('Все элемента списка в единичном экземпляре')
except ValueError:
    print('Вы ввели некорректное значение!')
