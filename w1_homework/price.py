"""
Задание 2
Создайте в редакторе файл price.py
Создайте функцию format_price, которая принимает один аргумент price
Приведите price к целому числу (тип int)
Верните строку "Цена: ЧИСЛО руб."
Вызовите функцию, передав на вход 56.24 и положите результат в переменную
Выведите значение переменной с результатом на экран
"""


def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'


format_price_result = format_price(56.24)
print(format_price_result)
