"""
Плагин «Пинг»

Ассистент проверяет есть ли доступ в интернет, рутем отправки пинг запросов на сайт ya.ru
В переменной `ping_url` можно изменить адрес сайта

"""
__author__ = 'rad-li'
__version__ = 0.2

import requests

ping_url = "https://ya.ru/"


def main(command):
    try:
        requests.get(ping_url)
        answer = "Интернет работает"
    except Exception:
        answer = "Нет доступа в интернет"

    return answer
