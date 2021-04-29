"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

with open("text_77.json", "w") as j_file:
    with open("text_7.txt", "r") as f_o:
        sub = {}
        analytics = {}
        t_profit, profit_comp = 0, 0
        lines = f_o.read().split("\n")
        for comp_info in lines:
            comp_info = comp_info.split()
            profit = int(comp_info[2]) - int(comp_info[3])
            sub[comp_info[0]] = profit
            if profit > 0:
                t_profit += profit
                profit_comp += 1
            analytics["average"] = t_profit / profit_comp
        all_list = [sub, analytics]
        json.dump(all_list, j_file)
