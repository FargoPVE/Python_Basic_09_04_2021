"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_time = int(input("Введите ваше время в секундах: "))
program_ss = user_time % 100
program_mm = (user_time // 60) % 100
program_hh = (user_time // 60) // 60

print(f"{program_hh:02} : {program_mm:02} : {program_ss:02}")