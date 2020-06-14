"""
    Задание 3.
    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, то надо вывести число 6843.
"""

try:
    num = int(input('Введите число: '))
    source_num = num
    result = 0

# Решение №1 (цикл)
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10

    print(f'Обратное число {source_num}: {result}')


# Решение №2 (рекурсия)


    def recursive_func(num, result):
        if num <= 0:
            return f'Обратное число {source_num}: {result}'
        else:
            return recursive_func(num // 10, result * 10 + num % 10)


    print(recursive_func(num, result))

except ValueError:
    print('Число введено некорректно!')
