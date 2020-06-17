'''
    Задание 7.
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
from random import randint

try:
    N = int(input('Введите количество элементов: '))
    arr = [int(randint(-100, 100)) for i in range(N)]

    if arr[0] > arr[1]:
        min1 = 0
        min2 = 1
    else:
        min1 = 1
        min2 = 0

    for i in range(2, N):
        if arr[i] < arr[min1]:
            temp = min1
            min1 = i
            if arr[temp] < arr[min2]:
                min2 = temp
        elif arr[i] < arr[min2]:
            min2 = i

    print(arr, end=' ')
    print()
    print(f'Наименьшие элементы в списке: {min1 + 1} = {arr[min1]} и {min2 + 1} = {arr[min2]}')

except ValueError:
    print('Некорректно введено значение')
except IndexError:
    print('Количество элементов не может быть меньше 2-х')