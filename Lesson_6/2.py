"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler.asizeof import asizeof


class MyClass1:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class MyClass2:

    __slots__ = ['name', 'last_name']

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


a = MyClass1('имя', 'фамилия')
b = MyClass2('имя', 'фамилия')

print(a.__dict__)
print(b.__slots__)
print(asizeof(a))
print(asizeof(b))
print(asizeof(a)/asizeof(b))

'''
Для класса с применением слотов в моём случае памяти выделяется в 2.0357142857142856 меньше, чем 
для класса без слотов. Но в классе со слотами нет возможности создать атрибуты динамически, например:
b.address = 'адрес' выдаст ошибку.
'''