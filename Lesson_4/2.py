"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit


def sie(lim, n):
    def sieve(n):
        a = [x for x in range(n + 1)]
        a[1] = 0
        lst = []
        i = 2
        while i <= n:
            if a[i] != 0:
                lst.append(a[i])
                for j in range(i, n + 1, i):
                    a[j] = 0
            i += 1
        return lst
    while len(sieve(n)) < lim:
        n += 1
    return sieve(n).pop()


def nai(lim, n):
    def naive_algo(n):
        # lst = [2]
        # for i in range(3, n + 1, 2):
        #     if (i > 10) and (i % 10 == 5):
        #         continue
        #     for j in lst:
        #         if j * j - 1 > i:
        #             lst.append(i)
        #             break
        #         if i % j == 0:
        #             break
        #     else:
        #         lst.append(i)
        # return lst
        lst = []
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    # если делитель найден, число не простое.
                    break
            else:
                lst.append(i)
        return lst
    while len(naive_algo(n)) < lim:
        n += 1
    return naive_algo(n).pop()


# lim = int(input("Введите номер простого числа: "))
# n = 2
#
#
# print(sie(lim, n))
# print(nai(lim, n))

print(timeit.timeit("sie(100, 2)", setup="from __main__ import sie", number=5))
print(timeit.timeit("nai(100, 2)", setup="from __main__ import nai", number=5))


'''
Попробовал измерить 3 варианта. Решето работает быстрее на большом порядковом номере простого числа.
Другие 2 алгоритма работают быстрее на маленьком порядковом номере простого числа(<5).

Замеры при lim = 100:
0.5556905659996119 - решето
4.0153251709998585 - наивный алгоритм

Со сложностью - затрудняюсь ответить, но могу предположить, что О(N log N) - линейно-логарифмическая
'''
