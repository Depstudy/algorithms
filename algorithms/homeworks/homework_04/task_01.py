'''
    Задание 1.
    Проанализировать скорость и сложность одного любого алгоритма,
    разработанных в рамках домашнего задания первых трех уроков.
'''
import timeit
import cProfile
import sys

sys.setrecursionlimit(100000)


# создам декоратор для мемоизации
def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


# Функция с рекурсией для подсчёта чётных и нечётных цифр введенного числа
# @memoize
def recursive_num(num_rec, even_rec, odd_rec):
    if num_rec == 0:
        return f'В числе {num_rec}, {even_rec} - четных и {odd_rec} - нечетных цифр'
    elif num_rec % 2 == 0:
        return recursive_num(num_rec // 10, even_rec + 1, odd_rec)
    elif num_rec % 2 != 0:
        return recursive_num(num_rec // 10, even_rec, odd_rec + 1)


# @memoize
def cycle_num(num, even, odd):
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


# Ещё одна функция с рекурсией из задания 4, урока 2
# @memoize
def recursion_sum(n, num, result):
    if n == 0:
        return f'Сумма {n} элементов равна: {result}'
    elif n > 0:
        num = num / -2
        return recursion_sum(n - 1, num, result + num)


# Цикл for из задания 4, урока 2
# @memoize
def cycle_for(n, num, result):
    for n in range(1, n + 1):
        num = num / -2
        result = result + num
    return result


def all_func():
    recursive_num(12345, 0, 0)
    cycle_num(12345, 0, 0)
    recursion_sum(5, -2, 0)
    cycle_for(5, -2, 0)


num_test = 1

print('='*25, f'Тест №{num_test}', '='*25)
result_1 = (
    round(timeit.timeit('recursive_num(12345, 0, 0)', 'from __main__ import recursive_num'), 2))
print(f'Результат теста функции с рекурсией № {num_test}: {result_1} сек.')
result_2 = (round(timeit.timeit('cycle_num(12345, 0, 0)', 'from __main__ import cycle_num'), 2))
print(f'Результат теста функции с циклом № {num_test}: {result_2} сек.')
print(f'По результатам теста № {num_test}, цикл работает быстрее рекурсии на {round((result_1 - result_2), 2)} сек.')
print()
print('='*25, f'Тест №{num_test+1}', '='*25)
result_1 = (round(timeit.timeit('recursion_sum(5, -2, 0)', 'from __main__ import recursion_sum'), 2))
print(f'Результат теста функции с рекурсией № {num_test+1}: {result_1} сек.')
result_2 = (round(timeit.timeit('cycle_for(5, -2, 0)', 'from __main__ import cycle_for'), 2))
print(f'Результат теста функции с циклом for № {num_test+1}: {result_2} сек.')
print(f'По результатам теста № {num_test+1}, цикл работает быстрее рекурсии на {round((result_1 - result_2), 2)} сек.')
print()

cProfile.run('all_func()')
#После профилировки всех функций результаты показали, что функции не нуждаются в оптимизации, однако при использовании
# мемоизации результаты тестов значительно улучшились.

"""
    Итог: Оптимизация через мемоизацию улучшает скорость выполнения кода в несколько раз
"""