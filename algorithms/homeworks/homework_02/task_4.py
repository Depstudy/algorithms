"""
    Задание 4.
    Найти сумму n элементов следующего ряда чисел:
    1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
import sys

sys.setrecursionlimit(10000)


# Решение 1 (рекурсия)
def recursion_sum(n, num, result):
    if n == 0:
        return f'Сумма {source_n} элементов равна: {result}'
    elif n > 0:
        num = num / -2
        return recursion_sum(n - 1, num, result + num)


try:
    n = int(input('Введите количесвто элементов: '))
    source_n = n  # Переменная для вывода количества элементов в рекурсивной функции
    num = -2
    result = 0

    '''
    # Решение 2 (цикл for)
    for n in range(1, n + 1):
        num = num / -2
        result = result + num

    print(f'Сумма {n} элементов равна: {result}')
    '''
    print(recursion_sum(n, num, result))

except ValueError:
    print('Некорректно введено число элементов!')
