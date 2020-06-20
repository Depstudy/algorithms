'''
    Задание 3
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
from random import random

N = int(input('Введите количество элементов: '))
arr = [0]*N

for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

mn = 0
mx = 0

for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print(f'Минимальный элемент: {mn + 1}-й равен: {arr[mn]}, максимальный элемент: {mx + 1}-й равен: {arr[mx]}')
print('Меняем местами минимальный и максимальный элементы...')

temp = arr[mn]
arr[mn] = arr[mx]
arr[mx] = temp

print('Результат:')
for i in range(N):
    print(arr[i], end=' ')
print()
