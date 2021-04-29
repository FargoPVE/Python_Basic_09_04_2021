"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
result = []
with open("text_3.txt", "r") as f_o:
    lines = f_o.readlines()
    for line in lines:
        name, money = line.split()
        money = float(money)
        result.append(money)
        if money < 20000:
            print(name)
    print(f"Средний доход сотрудников равен: {sum(result) / len(result)} руб.")
