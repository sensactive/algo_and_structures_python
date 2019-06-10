"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import sys


# s = input('введите строку из маленьких латинских букв: ')
# t = set()
#
# for i in range(len(s)):
#     for j in range(len(s) + 1):
#         if s[i:j] and s[i:j] != s:
#             t.add(s[i:j])
#
# print(sys.getsizeof(t))
# print(len(t))
#
import hashlib

s = input('введите строку из маленьких латинских букв: ')
t = set()

for i in range(len(s)):
    for j in range(len(s) + 1):
        if s[i:j] and s[i:j] != s:
            t.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(sys.getsizeof(t))
print(len(t))



'''
Абсолютно никакой разницы в размерах я не смог увидеть в этих двух подходах...(( 
'''