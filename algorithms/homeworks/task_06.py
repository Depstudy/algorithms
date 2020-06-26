'''
    Задание 6.
    В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать.
'''
from random import random

try:
    N = int(input('Введите количество элементов: '))
    arr = [int(random() * 50) for i in range(N)]
    min_num = 0
    max_num = 0
    summa = 0

    print(f'{arr}')

    for i in range(N):
        if arr[i] < arr[min_num]:
            min_num = i
        elif arr[i] > arr[max_num]:
            max_num = i

    print(f'Значение минимального элемента: {arr[min_num]}, максимального: {arr[max_num]}')

    if min_num > max_num:
        min_num, max_num = max_num, min_num

    for i in range(min_num+1, max_num):
        summa += arr[i]
    print(f'Сумма элементов между минимальным и максимальным элементами: {summa}')

except ValueError:
    print('Введено некорректное значение!')
