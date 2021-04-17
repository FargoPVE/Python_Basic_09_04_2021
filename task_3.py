"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons = ["Зима", "Весна", "Лето", "Осень"]
num_seasons = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

seasons_dict = {seasons[0]: num_seasons[0:3],
                seasons[1]: num_seasons[3:6],
                seasons[2]: num_seasons[6:9],
                seasons[3]: num_seasons[9:12]}

user_int = int(input("Введите число вашего месяца: "))

for key, value in seasons_dict.items():
    if user_int in value:
        print(key)
        break