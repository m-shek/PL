"""
Урок "Функции" func_delim.py
Задание 1
Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает объединенными через разделитель delimiter
Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
Сделайте так, чтобы результирующая строка выводилась заглавными буквами
"""


def get_summ(one, two, delimeter='&'):
    one = str(one)
    two = str(two)
    result = one + delimeter + two
    return result


get_sum_result = get_summ('Learn', 'python')
print(get_sum_result.upper())
