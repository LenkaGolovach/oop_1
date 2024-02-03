#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Time для работы со временем в формате «час:минута:секунда». Класс
должен включать в себя не менее четырех функций инициализации: числами, строкой
(например, «23:59:59»), секундами и временем. Обязатель ными операциями являются:
вычисление разницы между двумя моментами времени в секундах, сложение времени и
заданного количества секунд, вычи тание из времени заданного количества секунд,
сравнение моментов времени, перевод в секунды, перевод в минуты (с округлением до
целой минуты).
"""

import math

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__seconds = hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def from_string(time_str):
        parts = list(map(int, time_str.split(':')))
        return Time(parts[0], parts[1], parts[2])

    @staticmethod
    def from_seconds(seconds):
        return Time(0, 0, seconds)

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(':')))
        self.__seconds = parts[0] * 3600 + parts[1] * 60 + parts[2]

    def display(self):
        hours = self.__seconds // 3600
        minutes = (self.__seconds % 3600) // 60
        seconds = self.__seconds % 60
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def add_seconds(self, seconds):
        self.__seconds += seconds

    def subtract_seconds(self, seconds):
        self.__seconds -= seconds

    def difference(self, other):
        if isinstance(other, Time):
            return abs(self.__seconds - other.__seconds)
        else:
            raise ValueError()

    def compare(self, other):
        if not isinstance(other, Time):
            raise ValueError()
        return self.__seconds - other.__seconds

    def to_seconds(self):
        return self.__seconds

    def to_minutes(self):
        return math.floor(self.__seconds / 60)

if __name__ == '__main__':
    time1 = Time(1, 30, 15)
    time1.display()

    time2 = Time.from_string("2:45:30")
    time2.display()

    print("Разница между time1 и time2 в секундах:", time1.difference(time2))

    time1.add_seconds(500)
    time1.display()

    time2.subtract_seconds(300)
    time2.display()

    print("Time1 в секундах:", time1.to_seconds())
    print("Time2 в минутах:", time2.to_minutes())

    time3 = Time()
    time3.read("Введите время в формате чч:мм:сс: ")
    time3.display()

    comparison = "больше" if time1.compare(time3) > 0 else "меньше или равно"
    print(f"Введенное время {comparison} time1.")
