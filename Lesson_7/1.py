"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import timeit
from random import randint


def sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort_1(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr) - i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort_2(arr):
    i = 0
    t = True
    while t:
        t = False
        for j in range(i+1, len(arr) - i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                t = True
    return arr


arr = [randint(-100, 100) for _ in range(0, 15)]
print(arr)
print(sort(arr))
print(sort_1(arr))
print(sort_2(arr))

print(timeit.timeit(f'sort({arr})', setup="from __main__ import sort", number=10000))
print(timeit.timeit(f'sort_1({arr})', setup="from __main__ import sort_1", number=10000))
print(timeit.timeit(f'sort_2({arr})', setup="from __main__ import sort_2", number=10000))

'''
Второй способ работает в полтора раза быстрее, т.к. мы не проходим по тем элементам, которые уже "всплыли".
Третий способ работает в 10 раз быстрее первого, т.к. + ко 2-му способу цикл завершается, если не произошло
ни одной замены элементов.
'''