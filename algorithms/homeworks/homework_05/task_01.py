'''
    Задание 1.
    Пользователь вводит данные о количестве предприятий,
    их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
    Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
    чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
from collections import namedtuple

try:
    def profit(*cnt_profit):
        summa = 0
        for i in cnt_profit:
            for el in i:
                summa += int(el)
        return summa


    N = int(input('Введите количество предприятий для расчета прибыли: '))  # Количество предприятий
    profit_all_org = 0  # Переменная для расчета срденей годовой прибыли всех организаций
    org_list = []
    org_max = []
    org_min = []

    for i in range(N):
        name_organization = input('Введите название предприятия: ').title()
        prof = profit(input('Введите прибыль (через пробел) за 4 квартала: ').split(' '))  # Прибыль предприятия
        tup = namedtuple(f'Организация_{i+1}', 'name_org profit_org av_profit')
        org = tup(
            name_org=name_organization,
            profit_org=prof,
            av_profit=(prof/4)
        )
        profit_all_org = profit_all_org + org.profit_org
        org_list.append(org)

    profit_all_org = profit_all_org / N     # Расчет средней прибыли на количество предприятий

    for i in range(N):
        if org_list[i].profit_org > profit_all_org:
            org_max.append(org_list[i].name_org)
        else:
            org_min.append(org_list[i].name_org)

    print(f'Средняя прибыль за год у всех предприятий: {round(profit_all_org, 2)}')

    if len(org_max) > 1:
        print('Предприятия, с прибылью выше среднего:', end=' ')
        for el in org_max:
            print(f',{el}', end=' ')
        print()
    elif len(org_max) == 0:
        print('Нет предприятий с прибылью выше среднего')
    else:
        print(f'Предприятие, с прибылью выше среднего: {org_max[0]}')

    if len(org_min) > 1:
        print('Предприятия, с прибылью ниже среднего:', end=' ')
        for el in org_min:
            print(f'{el}', end=' ')
    elif len(org_min) == 0:
        print('Нет предприятий с прибылью выше среднего')
    else:
        print(f'Предприятия, с прибылью ниже среднего: {org_min[0]}')
except ValueError:
    print('Неверно введено значение!')

