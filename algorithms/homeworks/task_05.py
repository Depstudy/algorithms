'''
    Задание 5.
    В массиве найти максимальный отрицательный элемент.
    Вывести на экран его значение и позицию в массиве.
'''
from random import randint

try:
    N = int(input('Введите количество элементов: '))
    arr = [int(randint(-100, 100)) for i in range(N)]
    index = -1

    print(arr)

    for i in range(N):
        if arr[i] < 0 and index == -1:
            index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
            index = i
        i += 1

    print(f'Максимальный отрицательный элемент: {index + 1}, значение которого: {arr[index]}')
except ValueError:
    print('Некорректно введено значение!')
