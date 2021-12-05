"""
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""

from os import pipe
content =''
line_words =[]
line_len = 0
text =[]

with open('files\\referat.txt', 'r', encoding='utf-8') as myfile:
    for line in myfile:
        content += line.replace(".", "!")  
        line_words += line.split()
        line_len += len(line_words)

with open('files\\referat2.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(content)

print(f'Количество символов в тексте: {len(content)}')
print(f'Количество слов в тексте: {line_len}')