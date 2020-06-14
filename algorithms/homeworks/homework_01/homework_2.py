"""
    Задание 2
    Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
    Объяснить полученный результат.
"""

num_1 = 5
num_2 = 6

bit_or = num_1 | num_2
bit_and = num_1 & num_2
bit_xor = num_1 ^ num_2

print(bit_or)   # Выполнение операции "ИЛИ"
print(bit_and)  # Выполнение операции "И"
print(bit_xor)  # Выполнение операции "Исключающее ИЛИ"

print(f'Побитовый сдвиг числа {num_1} на два знака влево: {num_1 << 2}')
# Оператор << выполняет поразрядовый сдвиг влево, где значение левого операнда будет перемещено влево на число бит,
# заданное правым операндом. Это означает что num_1 << n = num_1 * 2^n (2 ** n)
print(f'Побитовый сдвиг числа {num_1} на два знака вправо: {num_1 >> 2}')
# Оператор >> выполняет поразрядовый сдвиг влево, где значение левого операнда будет перемещено влево на число бит,
# заданное правым операндом. Это означает что num_1 >> n = num_1 / 2^n (2 ** n)
