"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

program_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"}

with open("text_4.txt", "r") as f_o:
    with open("text_4_2.txt", "w") as final_file:
        lines = f_o.readlines()
        for line in lines:
            num_list = line.split(" - ")
            final_file.write(f"{program_dict[num_list[0]]} - {num_list[1]}")

with open("text_4_2.txt", "r") as f_o_2:
    lines_2 = f_o_2.read()
    print(lines_2)