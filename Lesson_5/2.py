"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

mas = input('Введите первое шестнадцатиричное число: ')
mbs = input('Введите второе шестнадцатиричное число: ')

ma = []
mb = []

for s in mas:
    ma.append(s)

for s in mbs:
    mb.append(s)

a = '0x'
b = '0x'

for i in ma:
    a += i

for i in mb:
    b += i

a, b = int(a, 16), int(b, 16)
c, d = hex(a + b), hex(a * b)

summ = deque()
mult = deque()

for i in range(2, len(c)):
    summ.append(c[i].upper())

for i in range(2, len(d)):
    mult.append(d[i].upper())

print(f'Для чисел {ma} и {mb} сумма равна {summ}, произведение равно{mult}')
