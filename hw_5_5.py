"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("text_5.txt", "w") as f_o:
    num = f"{input('Введите ваши числа через пробел: ')}"
    f_o.write(num)

with open("text_5.txt", "r") as f_o:
    lines = f_o.readline()
    my_list = map(int, lines.split())
    print(sum(my_list))