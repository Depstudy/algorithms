"""
    Задание 2.
    Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
import sys

sys.setrecursionlimit(10000)

try:
    num = int(input('Введите число: '))
    source_num = num
    even = 0
    odd = 0


    # Вариант 1 (Решение через рекурсию)

    def recursive_num(num_rec, even_rec, odd_rec):
        if num_rec == 0:
            return f'В числе {source_num}, {even_rec} - четных и {odd_rec} - нечетных цифр'
        elif num_rec % 2 == 0:
            return recursive_num(num_rec // 10, even_rec + 1, odd_rec)
        elif num_rec % 2 != 0:
            return recursive_num(num_rec // 10, even_rec, odd_rec + 1)


    print(recursive_num(num, even, odd))

    # Вариант 2 (Решение через цикл)
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10

    print(f'В числе {source_num}, {even} - четных и {odd} - нечетных цифр')
except ValueError:
    print('Число введено некорректно!')
