"""
    Задание 7
    По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
    составленного из этих отрезков.
    Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
# Создаем 3 переменные с длинами отрезков
line_1 = int(input('Введите длину первого отрезка: '))
line_2 = int(input('Введите длину второго отрезка: '))
line_3 = int(input('Введите длину второго отрезка: '))

# Треугольник существует только когда сумма любых двух его сторон больше третьей
if line_1 + line_2 <= line_3 or line_1 + line_3 <= line_2 or line_2 + line_3 <= line_1:
    print('Треугольник не существует')
# Треугольник является разносторонним, если все его стороны имеют разную длину
elif line_1 != line_2 and line_1 != line_3 and line_2 != line_3:
    print('Треугольник является разносторонним')
# Треугольник будет равносторонним если все его стороны равны
elif line_1 == line_2 == line_3:
    print('Треугольник является равносторонним')
# Треугольник будет равнобедренным, если две его стороны равны, но отличны от третьей
else:
    print('Треугольник является равнобедренным')