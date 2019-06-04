"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile


# @profile
# def sie(lim, n):
#     def sieve(n):
#         a = [x for x in range(n + 1)]
#         a[1] = 0
#         lst = []
#         i = 2
#         while i <= n:
#             if a[i] != 0:
#                 lst.append(a[i])
#                 for j in range(i, n + 1, i):
#                     a[j] = 0
#             i += 1
#         return lst
#     while len(sieve(n)) < lim:
#         n += 1
#     return sieve(n).pop()
#
#
# @profile
# def nai(lim, n):
#     def naive_algo(n):
#         # lst = [2]
#         # for i in range(3, n + 1, 2):
#         #     if (i > 10) and (i % 10 == 5):
#         #         continue
#         #     for j in lst:
#         #         if j * j - 1 > i:
#         #             lst.append(i)
#         #             break
#         #         if i % j == 0:
#         #             break
#         #     else:
#         #         lst.append(i)
#         # return lst
#         lst = []
#         for i in range(2, n + 1):
#             for j in range(2, i):
#                 if i % j == 0:
#                     # если делитель найден, число не простое.
#                     break
#             else:
#                 lst.append(i)
#         return lst
#     while len(naive_algo(n)) < lim:
#         n += 1
#     return naive_algo(n).pop()
#
#
# lim = 20
# n = 2
#
#
# print(sie(lim, n))
# print(nai(lim, n))

@profile
def function1():
    a = [i for i in range(10000)]
    # 1.
    max_value = int()
    min_value = a[0]
    for i in a:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i
    a[a.index(max_value)], a[a.index(min_value)] = a[a.index(min_value)], a[a.index(max_value)]


@profile
def function2():
    a = [i for i in range(10000)]
    # 2.
    a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
    a = None


if __name__ == "__main__":
    function1()
    function2()
'''
Python 3.6.7
x64 (Ubuntu)
На моем коде решета Эратосфена замеры неинформативные((( Предположу, что это из-за рекурсии.
Пробовал подставлять разные значения. Всегда вначале выделяется 14.4 MiB и всё(А может быть у меня такой
алгоритм, что расходуется мало памяти?). Далее взял другой код и инкремент стал появляться при создании 
списка с числами от 0 до 10000 (+0.2 MiB). После a = None -> -0.2.
 

'''