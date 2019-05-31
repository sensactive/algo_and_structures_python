"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import deque, namedtuple

# вариант 1

companies = {}
number = int(input('Введите количество предприятий: '))

for i in range(number):
    name = input('Введите наименование предприятия')
    companies[name] = []

    for q in range(4):
        profit = int(input('Введите прибыль предприятия за квартал: '))
        companies[name].append(profit)

counting = {}
average = 0
for i in companies:
    profit = 0
    for p in companies[i]:
        profit += p
    counting[i] = profit
    average += profit

average = average / number

below = deque()
above = deque()

for i in counting:
    if counting[i] < average:
        below.append(i)
    else:
        above.append(i)

print(f'Предприятия с прибылью выше среднего {above} предприятия с прибылью ниже среднего {below}')

# вариант 2

firms = {}
num = int(input('Введите количество предприятий: '))

firm = namedtuple('firm', 'name first_q second_q third_q forth_q')
for i in range(num):
    firms[i] = firm(
        name=input('Введите наименование предприятия'),
        first_q=int(input('Введите прибыль предприятия за первый квартал: ')),
        second_q=int(input('Введите прибыль предприятия за второй квартал: ')),
        third_q=int(input('Введите прибыль предприятия за третий квартал: ')),
        forth_q=int(input('Введите прибыль предприятия за четвертый квартал: '))
    )

firms_tot = {}
ave = 0
for i in range(num):
    firms_tot[firms[i].name] = firms[i].first_q + firms[i].second_q + firms[i].third_q + firms[i].forth_q
    ave += firms[i].first_q + firms[i].second_q + firms[i].third_q + firms[i].forth_q
ave = ave / num

bel = deque()
abo = deque()

for i in firms_tot:
    if firms_tot[i] < ave:
        bel.append(i)
    else:
        abo.append(i)

print(f'Предприятия с прибылью выше среднего {abo} предприятия с прибылью ниже среднего {bel}')