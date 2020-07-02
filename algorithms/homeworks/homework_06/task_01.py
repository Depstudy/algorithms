'''
    Задание 1.
    Подсчитать, сколько было выделено памяти под переменные в
    ранее разработанных программах в рамках первых трех уроков.
    Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''
from memory_profiler import profile
from sys import getrefcount
from copy import deepcopy


@profile
def recursive_num(num_rec, even_rec, odd_rec):
    if num_rec == 0:
        return f'В числе {num_rec}, {even_rec} - четных и {odd_rec} - нечетных цифр'
    elif num_rec % 2 == 0:
        return recursive_num(num_rec // 10, even_rec + 1, odd_rec)
    elif num_rec % 2 != 0:
        return recursive_num(num_rec // 10, even_rec, odd_rec + 1)


recursive_num(12345, 0, 0)
# Функции с рекурсией выделяется под profile примерно от 13.4 MiB до 13.6 MiB
# В дальнейшем количество памяти не меняется


@profile
def cycle_num(num, even, odd):
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


cycle_num(12345, 0, 0)
# C циклом ситуация такая же как и с рекурсивной функцией, во время выполнения выделяется от 13.4 до 13.6 MiB
# Видимо это связано с тем, что сами функции не хранят переменные, а принимают их на вход, выполняют вычисления и
# возвращают результат


@profile
def new_func():
    my_list = list(range(90000))
    new_list = deepcopy(my_list)
    print(getrefcount(my_list))
    del my_list, new_list


new_func()
# В случае с этой функцией во время выполнения изначально выделяется от 13.4 до 13.6 MiB
# В дальнейшем при создании переменной со списком выделяется ещё примерно 3.4 MiB
# При создании новой переменной и копировании в неё списка выделяется ещё примерно 0.9 MiB
# На объект my_list создается 3 ссылки, 1 ссылка - во время создания самого объекта,
# 2 ссылка во время выполнения функции 'getrefcount()', 3 ссылка видимо сама функция.
# При использовании del память с 18.0 MiB освобождается до 14.0 MiB так как удаляются все ссылки на объект


@profile
def new_func_2():
    my_list = [el for el in range(90000)]
    new_list = deepcopy(my_list)
    print(getrefcount(my_list))


new_func_2()
# При такой функции показатели используемой памяти такие же как и у new_func(),
# однако на этапе использования генератора инкрементируется всего лишь 0.3 MiB, а не 3.4 MiB
# Почему такая погрешность или выделение памяти под генериратор считается иначе?

@profile
def new_func_3():
    print(list(range(900001)))


new_func_3()
# Функция генерирует массив, выводит его, но не сохраняет результат, следовательно не требует дополнительной памяти.
# Такая функция работает значительно быстрее остальных и не расходует дополнительных ресурсов оперативной памяти

my_list_2 = list(range(90000))
new_list_2 = deepcopy(my_list_2)
print(getrefcount(my_list_2))
# При выполнении кода вне функции, ссылок становится всего 2,
# т.к. new_list_2 = deepcopy(my_list_2) создает новый объект, а не ссылку на существующий

# Версия Python 3.8, разрядность ОС x64