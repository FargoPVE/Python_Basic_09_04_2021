"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def my_f(time, stavka, prem):
    return time * stavka + prem


print(f"Заработная плата равна: {my_f(*map(float, argv[1:]))} руб.")
