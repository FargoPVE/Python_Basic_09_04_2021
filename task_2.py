"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_input = input("Введите ваши значения: ")
my_list = user_input.split()

i = 0
while i < len(my_list[:-1]):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2
print(my_list)

# Второй вариант:
for x in my_list:
    if i < len(my_list[:-1]):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
print(my_list)