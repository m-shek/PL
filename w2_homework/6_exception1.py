"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    while True:
        try:
            how_are_you = input('Как дела? \n')
        except KeyboardInterrupt:
            print("Пока!")
            break

        if how_are_you == 'Хорошо':
            return False


if __name__ == "__main__":
    hello_user()
