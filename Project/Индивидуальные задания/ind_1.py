#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое число, левая граница диапазона, включается в диапазон; поле second —
целое число, правая граница диапазона, не включается в диапазон. Пара чисел
представляет полуоткрытый интервал [first, second). Реализовать метод rangecheck() —
проверку заданного целого числа на принадлежность диапазону.
"""

class Pair:
    def __init__(self, first=0, second=0):
        first = int(first)
        second = int(second)

        if first >= second:
            raise ValueError("Значение 'first' должно быть меньше 'second'.")

        self.__first = first
        self.__second = second

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(', ', maxsplit=1)))

        if parts[0] >= parts[1]:
            raise ValueError("Первое значение должно быть меньше второго.")

        self.__first, self.__second = parts

    def display(self):
        print(f"[{self.__first}, {self.__second})")

    def rangecheck(self, value):
        value = int(value)
        return self.__first <= value < self.__second


def make_pair(first, second):
    """
    Функция создания экземпляра класса Pair, принимая значения полей как аргументы
    """
    return Pair(first, second)


if __name__ == '__main__':
    pair = make_pair(0, 10)  # Создание пары с начальными значениями
    pair.display()  # Вывод созданной пары

    print("Введите два числа через запятую для создания интервала (например, '5, 10'): ")
    pair.read("Введите интервал: ")
    pair.display()  # Вывод введённой пары

    value = int(input("Введите значение для проверки принадлежности к интервалу: "))
    if pair.rangecheck(value):
        print(f"Значение {value} находится в интервале.")
    else:
        print(f"Значение {value} находится вне интервала.")
