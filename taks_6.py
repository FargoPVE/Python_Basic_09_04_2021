"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
"""

name = "название"
price = "цена"
lot = "колличество"
unit = "единица измерения"
unit_program = "ед."

program_name = []
program_price = []
program_lot = []
program_unit = []

user_dict = {}

my_analytics_dict = {name: program_name, price: program_price, lot: program_lot, unit_program: program_unit}

my_tuple_1 = (1, user_dict)
my_tuple_2 = (2, user_dict)
my_tuple_3 = (3, user_dict)

my_list = [my_tuple_1, my_tuple_2, my_tuple_3]

for x in my_list:
    print(f"Введите информацию о Вашем {x[0]} товаре")
    user_name = input(f"Введите {name} товара: ").lower()
    user_dict[name] = user_name
    program_name.append(user_name)
    user_price = float(input(f"Какова {price} товара: "))
    user_dict[price] = user_price
    program_price.append(user_price)
    user_lot = int(input(f"Введите {lot} товара: "))
    user_dict[lot] = user_lot
    program_lot.append(user_lot)
    user_unit = input(f"Какова {unit}: ").lower()
    user_dict[unit] = user_unit
    program_unit.append(user_unit)

print(f"Данные товара: {my_list}")
print(f"Аналитика товаров: {my_analytics_dict}")
