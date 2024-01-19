#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Point:

    def __init__(self, x=0, y=0):
        x = float(x)
        y = float(y)

        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # Прочитать координаты с клавиатуры
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(' x ', maxsplit=1)))

        if parts[1] == 0:
            raise ValueError()

        self.__x = parts[0]
        self.__y = parts[1]

    # Вывести координаты на экран
    def display(self):
        print(f"{self.__x} x {self.__y}")

    # Перемещение по х
    def move_x(self, step):
        self.__x = self.__x + step

    # Перемещение по у
    def move_y(self, step):
        self.__y = self.__y + step

    # Расстояние до начала координат
    def dist_to_zero(self):
        return math.sqrt(pow(self.__x, 2) + pow(self.__y, 2))

    # Расстояние между точками
    def distance(self, coords):
        if isinstance(coords, Point):
            return math.sqrt(pow(self.__x - coords.__x, 2) + pow(self.__y - coords.__y, 2))
        else:
            return False

    # Преобразование в полярные координаты
    def polar(self):
        r = self.dist_to_zero()
        f = math.atan(self.__y / self.__x)
        return str(f"({r},{f}°)")

    # Проверка на совпадение
    def is_similar(self, coords):
        if isinstance(coords, Point):
            if self.__x == coords.__x and self.__y == coords.__y:
                return "Точки совпадают"
            else:
                return "Точки не совпадают"
        else:
            raise ValueError()


if __name__ == '__main__':
    c1 = Point(3.5, 1.4)
    c1.display()

    c2 = Point()
    c2.read("Введите координаты: ")
    c2.display()

    c1.move_x(-2)
    c1.display()

    c2.move_y(1.5)
    c2.display()

    print(c1.dist_to_zero())
    print(c2.polar())

    print(c1.distance(c2))
    print(c2.is_similar(c1))