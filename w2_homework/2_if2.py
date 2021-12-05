"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""


def compare_strings(str1, str2):
    if not (isinstance(str1, str)) or not (isinstance(str2, str)):
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3


def main():
    print(compare_strings('sdfsdf', 2))  # 0
    print(compare_strings(True, 'строка'))  # 0
    print(compare_strings(None, 2.56))  # 0
    print(compare_strings('дубликат', 'дубликат'))  # 1
    print(compare_strings('learn', "learn"))  # 1
    print(compare_strings('long string', 'learn'))  # 2
    print(compare_strings('разные строки', 'вторая строка длиннее'))  # None?
    print(compare_strings('2', 'learn'))  # 3


if __name__ == "__main__":
    main()
