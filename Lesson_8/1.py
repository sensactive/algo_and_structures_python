"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque


# Функция формирует и возвращает бинарное дерево
def tree(d):
    left = d.popleft()
    right = d.popleft()
    node = ((left, right), left[1] + right[1])
    if len(d) == 1:
        d.append(node)
        return d
    for i in range(len(d)):
        if node[1] <= d[i][1]:
            d.insert(i, node)
            break
        elif i == len(d) - 1:
            d.append(node)
    return tree(d)


# Обход бинарного дерева до элемента и запись в словарь элемента с его кодом
def make_codes(tree, code=''):
    if len(tree[0]) == 1:
        codes[tree] = code
        return
    l, r = tree[0], tree[1]
    make_codes(l[0], code=f'{code+"0"}')
    make_codes(r[0], code=f'{code+"1"}')


s = 'beep boop beer!'
a = Counter(s)
d = deque(sorted(a.items(), key=lambda t: t[1]))
codes = dict()
make_codes(tree(d))
for char in s:
    print(codes[char], end=' ')


'''
У меня получилось немного не так, как в методичке...Коды символов ' ' и 'o' поменялись местами, т.к. после
сортировки коллекции сначала идет пробел, а потом 'o'. Получается, что конечный код очень зависит от того,
как именно отсортируются элементы с одинаковым кол-вом вхождений в строку.
'''