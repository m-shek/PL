"""
Задание dicts.py
Создайте словарь:
{"city": "Москва", "temperature": "20"}
Выведите на экран значение ключа city
Уменьшите значение "temperature" на 5
Выведите на экран весь словарь
"""
dicts = {
    "city": "Москва",
    "temperature": "20"
}

print(dicts["city"])
dicts["temperature"] = str(int(dicts["temperature"]) - 5)
print(dicts)
