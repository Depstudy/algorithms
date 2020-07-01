'''
    Задание 2.
    Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
    заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
from random import random
from timeit import timeit


#
def sorting(arr):
    if len(arr) == 1:
        return
    midd = len(arr) // 2
    l_arr = arr[:midd]
    r_arr = arr[midd:]

    sorting(l_arr)
    sorting(r_arr)

    left_i, right_i, midd_i = 0, 0, 0
    while left_i < len(l_arr) and right_i < len(r_arr):
        if l_arr[left_i] < r_arr[right_i]:
            arr[midd_i] = l_arr[left_i]
            left_i += 1
        else:
            arr[midd_i] = r_arr[right_i]
            right_i += 1
        midd_i += 1

    for i in range(left_i, len(l_arr)):
        arr[midd_i] = l_arr[i]
        midd_i += 1

    for i in range(right_i, len(r_arr)):
        arr[midd_i] = r_arr[i]
        midd_i += 1

    return arr


#
def merger(mass):
    if len(mass) < 2:
        return mass[:]
    else:
        left_mass = merger(mass[:len(mass)//2])
        right_mass = merger(mass[len(mass)//2:])
        return merger_help(left_mass, right_mass)


def merger_help(left_side, right_side):
    answ = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_side) and right_idx < len(right_side):
        if left_side[left_idx] < right_side[right_idx]:
            answ.append(left_side[left_idx])
            left_idx += 1
        elif left_side[left_idx] > right_side[right_idx]:
            answ.append(right_side[right_idx])
            right_idx += 1
        else:
            answ.append(right_side[right_idx])
            answ.append(left_side[left_idx])
            right_idx += 1
            left_idx += 1
    while left_idx < len(left_side):
        answ.append(left_side[left_idx])
        left_idx += 1
    while right_idx < len(right_side):
        answ.append(right_side[right_idx])
        right_idx += 1
    return answ


#
def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


N = int(input('Введите количество элементов:'))
my_list = [random()*50 for n in range(N)]
my_list_2 = my_list.copy()
my_list_3 = my_list.copy()
print(f'Исходный - {my_list}')
result = round(timeit('merge_sort(my_list)', 'from __main__ import merge_sort, my_list', number=1000), 3)
print(f'{result} сек.')
print(f'Отсортированный - {merge_sort(my_list)}')

print(f'Исходный - {my_list_2}')
result = round(timeit('merger(my_list_2)', 'from __main__ import merger, my_list_2', number=1000), 3)
print(f'{result} сек.')
print(f'Отсортированный - {merger(my_list_2)}')

print(f'Исходный - {my_list_3}')
result = round(timeit('sorting(my_list_3)', 'from __main__ import sorting, my_list_3', number=1000), 3)
print(f'{result} сек.')
print(f'Отсортированный - {sorting(my_list_3)}')

# Функция merge_sort: |10 эл. - 0.017 сек.|    |100 эл. - 0.205 сек.|   |1000 эл. - 2.653 сек.|
# Функция merger:     |10 эл. - 0.018 сек.|    |100 эл. - 0.277 сек.|   |1000 эл. - 3.771 сек.|
# Функция sorting:    |10 эл. - 0.016 сек.|    |100 эл. - 0.212 сек.|   |1000 эл. - 2.78 сек|
#
# В полученных результат видно, что функция 'merge_sort' наиболее производительна,
# на втором месте по производительности с незначительной разницей в несколько сотых секунд находится функция 'sorting'.
# Функция 'merger' по полученным результатам оказалась самой 'медленной', особенно при большом количестве элементов
