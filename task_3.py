"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*cheat):
    """первый способ"""
    return sum(cheat) - min(cheat)


print(my_func(19, 6, 12))


def my_func_2(s_1, s_2, s_3):
    """второй способ"""
    return max(sum([s_1, s_2]), sum([s_2, s_3]), sum([s_1, s_3]))


print(my_func_2(15, 11, 22))
