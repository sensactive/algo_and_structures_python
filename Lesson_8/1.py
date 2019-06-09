"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque


a = Counter('beep boop beer!')
d = deque(sorted(a.items(), key=lambda t: t[1]))
left = d.popleft()
right = d.popleft()
node = ((f'{left[0]}', f'{right[0]}'), f'{left[1] + right[1]}')
d.appendleft(node)
print(d)
print(left, right)
print(node)
