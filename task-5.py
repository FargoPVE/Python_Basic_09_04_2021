"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [15, 12, 10, 10, 8, 7, 5, 3, 3, 3, 2, 2]

user_num = int(input("Введите ваше число: "))

for x in my_list:
    if user_num == my_list[0]:
        y = my_list.count(user_num)
        my_list.insert(y, user_num)
    elif user_num > my_list[0]:
        my_list.insert(0, user_num)
    elif user_num < my_list[-1]:
        my_list.append(user_num)
    elif user_num not in my_list:
        for x in my_list:
            i = my_list.index(user_num - 1)
            my_list.insert(i, user_num)
            break
    else:
        x = my_list.index(user_num) + my_list.count(user_num)
        my_list.insert(x, user_num)
    break
print(my_list)


