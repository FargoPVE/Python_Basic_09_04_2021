"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("text_1_task_2.txt", "r") as f_o:
    lines = f_o.readlines()
    print(f"Строк в файле: {len(lines)}")
    for i in lines:
        print(f"В строке: {i[:-1].upper()} - {len(i)} слов")
