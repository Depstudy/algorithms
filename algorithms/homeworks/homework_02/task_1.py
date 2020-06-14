'''
    Задание 1.
    Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
    Числа и знак операции вводятся пользователем.
    После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
    Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
    Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
     то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
    Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''

def calc(num1, sign, num2):
    result = 0
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '/':
        result = num1 / num2
    return result


answer = ''

while True:
    print('==================/Калькулятор/==================')
    print('Введите два числа и знак операции: \'+\' \'-\' \'*\' \'/\' или \'0\' для выхода')
    sign = input('Введите знак операции: ')
    if sign != '+' and sign != '-' and sign != '*' and sign != '/' and sign != '0':
        print('Знак операции введен не корректно!')
    elif sign == '0':
        print('Выход...')
        break
    else:
        try:
            while True:
                num1 = int(input('Введите первое число: '))
                num2 = int(input('Введите второе число: '))
                if num2 == 0 and sign == '/':
                    print('На ноль делить нельзя')
                else:
                    print(f'{num1} {sign} {num2} =', calc(num1, sign, num2))
                    break
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except ValueError:
            print('Необходимо вводить только числа')
