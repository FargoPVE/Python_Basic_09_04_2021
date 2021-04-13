"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

user_num = int(input("Введите ваше число: "))

program_num = str(user_num)
num_1 = program_num + program_num
num_2 = num_1 + program_num

result_num = user_num + int(num_1) + int(num_2)
print("Итоговое значение:", result_num)

