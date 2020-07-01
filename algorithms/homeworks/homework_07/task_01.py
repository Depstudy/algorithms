'''
    Задание 1.
    Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
    заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
    Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
'''
from random import randint
from timeit import timeit


# Классический вариант
def sort_func(my_list):
    a = 1
    while a < len(my_list):
        for i in range(len(my_list)-a):
            if my_list[i] < my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        a += 1
    return my_list


# "Умный" вариант
def sort_func_2(my_list):
    no_sort = True
    a = 1
    while a < len(my_list):
        for i in range(len(my_list)-a):
            if my_list[i] < my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                no_sort = False
        if no_sort == True:
            break
        a += 1
    return my_list


try:
    N = int(input('Введите количество элементов: '))
    my_list = [int(randint(-100, 100)) for n in range(N)]
    my_list_2 = my_list.copy()

    print(my_list)
    result = round(timeit('sort_func(my_list)', 'from __main__ import sort_func, my_list', number=1000), 3)
    print(f'{result} сек.')
    print(my_list)
    result = round(timeit('sort_func_2(my_list_2)', 'from __main__ import sort_func_2, my_list_2', number=1000), 3)
    print(f'{result} сек.')
    print(my_list_2)
except ValueError:
    print('Некорректно введено значение!')

# "Умный" вариант сортировки значительно быстрее классического, т.к. если все элементы уже отсортированы флаг 'no_sort'
# завершает работу цикла
#
# Классический вариант: 10 элементов - 0.01 сек, 100 эл. - 0.41 сек, 1000 эл. - 42.77 сек
# "Умный" вариант: 10 элементов - 0.001 сек, 100 эл. - 0.008 сек, 1000 эл. - 0.18 сек
