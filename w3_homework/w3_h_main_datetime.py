'''
Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime
'''

from datetime import datetime, timedelta

dt_now = datetime.now()
dt_yesterday = datetime.now() - timedelta(days=1)
dt_month_ago = datetime.now() - timedelta(days=30)

print(f'Вчера: {dt_yesterday.strftime("%d-%m-%Y")}')
print(f"Сегодня: {dt_now.strftime('%d-%m-%Y')}")
print(f'30 дней назад: {dt_month_ago.strftime("%d-%m-%Y")}')

another_date_sring ='01/01/25 12:10:03.234567'
another_date_print_format = datetime.strptime(another_date_sring,'%y/%m/%d %H:%M:%S.%f')
print(f'Дата из строки: {another_date_print_format}')