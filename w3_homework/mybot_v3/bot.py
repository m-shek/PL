"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import datetime
import ephem
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def get_planet(update, context):
    print("Вызван /planet")
    update.message.reply_text('Введите название планеты')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def find_planet(update, context):
    text = update.message.text
    text_cap = text.capitalize()
    today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    if text_cap == 'Mars' or text_cap == 'Марс':
        planets = ephem.Mars(today)

    elif text_cap == 'Jupiter' or text_cap == 'Юпитер':
        planets = ephem.Jupiter(today)

    elif text_cap == 'Mercury' or text_cap == 'Меркурий':
        planets = ephem.Mercury(today)

    elif text_cap == 'Venus' or text_cap == 'Венера':
        planets = ephem.Venus(today)

    elif text_cap == 'Earth' or text_cap == 'Земля':
        planets = ephem.Earth(today)

    elif text_cap == 'Saturn' or text_cap == 'Сатурн':
        planets = ephem.Saturn(today)

    elif text_cap == 'Uranus' or text_cap == 'Уран':
        planets = ephem.Uranus(today)

    elif text_cap == 'Neptune' or text_cap == 'Нептун':
        planets = ephem.Neptune(today)

    elif text_cap == 'Pluton' or text_cap == 'Pluto' or text_cap == 'Плутон':
        planets = ephem.Pluto(today)      
    else:
        planets_out = {"0","Планета не определена"}
    
    planets_out = ephem.constellation(planets)
    return update.message.reply_text(planets_out[1])


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, find_planet))
    #  dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
