#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Exp:

    def __init__(self, a=0, b=0):
        a = float(a)
        b = int(b)

        self.__first = a
        self.__second = b

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    # Прочитать значение
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(' ^ ', maxsplit=1)))

        self.__first = float(parts[0])
        self.__second = int(parts[1])

    # Вывести на экран
    def display(self):
        print(f"{self.__first} ^ {self.__second}")

    # Возведение в степень
    def power(self):
        return self.__first ** self.__second


def make_exp(first, second):
    """
    Функция создания экземпляра класса Pair, принимая значения полей как аргументы
    """
    return Exp(first, second)


if __name__ == '__main__':
    exm1 = Exp()
    exm1.read("Введите степень: ")
    exm1.display()

    exm2 = exm1.power()
    print(exm2)