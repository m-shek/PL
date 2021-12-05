"""
Задание dicts_country.py
Проверьте, есть ли в словаре ключ country
Выведите значение по-умолчанию "Россия" для ключа country
Добавьте в словарь элемент date со значением "27.05.2019"
Выведите на экран длину словаря
"""

dicts = {
    "city": "Москва",
    "temperature": "20"
}

print(f'Значение ключа country {dicts.get("country")}')
print(f'Значение ключа country по умолчанию изменено на {dicts.get("country", "Россия")}')
dicts["date"] = "27.05.2019"

print(f' Длина словаря {len(dicts)}')
