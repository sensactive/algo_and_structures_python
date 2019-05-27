"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
import timeit
from random import randint

a = [randint(1, 100) for i in range(100)]


# 1.


def inc_funcs():
    max_cnt_value = int()
    for i in a:
        if a.count(i) > a.count(max_cnt_value):     # вариант со встроенной функцией
            max_cnt_value = i
    # print(max_cnt_value)


# 2.


def count_with_set():
    c = 0
    max_cnt = int()
    max_cnt_idx = int()
    cnt = int()
    b = set(a)
    for i in b:
        for c in a:                     # вариант с использованием множества
            if i == c:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_cnt_idx = a.index(i)
        cnt = 0
        # print(2, end=' ')
    # print(a[max_cnt_idx], end=' ')


# 3.


def count_max():
    cnt = 0
    max_cnt = int()
    max_cnt_idx = int()
    for i in a:
        for c in a:                    # вариант без использования множества
            if i == c:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_cnt_idx = a.index(i)
        cnt = 0
        # print(1, end=' ')
    # print(a[max_cnt_idx], end=' ')


print(timeit.timeit("inc_funcs()", setup="from __main__ import inc_funcs", number=5))
print(timeit.timeit("count_with_set()", setup="from __main__ import count_with_set", number=5))
print(timeit.timeit("count_max()", setup="from __main__ import count_max", number=5))


'''
Сделал замеры трех разных алгоритмов поиска наиболее часто встречающегося числа в массиве.
Результат меня удивил. Алгоритм №2 с использованием множества, написанный мной работает быстрее,
чем алгоритм с использованием встроенной ф-ции №1 в 1.5 раза и в 2 раза быстрее, чем алгоритм №3.
Здесь О(n) - линейная сложность.

Замеры:
0.004881687000306556 №1
0.003929732999495172 №2
0.006941473000551923 №3
'''
