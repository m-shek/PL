"""
Создайте список словарей:
[
     {'name': 'Маша', 'age': '25', 'job': 'Scientist'},
     {'name': 'Вася', 'age': '8', 'job': 'Programmer'},
     {'name': 'Эдуард', 'age': '48', 'job': 'Big boss'}
]
Запишите содержимое списка словарей в файл в формате csv
"""
import csv

list_dict = [
    {'name': 'Маша', 'age': '25', 'job': 'Scientist'},
    {'name': 'Вася', 'age': '8', 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': '48', 'job': 'Big boss'}
]

with open('files_output\\export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = list_dict[0].keys()
    print(fields)
    writer = csv.DictWriter(f, fields)
    writer.writeheader()

    for record in list_dict:
        writer.writerow(record)
