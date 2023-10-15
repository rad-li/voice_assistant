"""
Плагин «Приветствие»

Ассистент произносит приветственные фразы.
"""

__author__ = 'rad-li'
__version__ = 0.2

import datetime
import random


def main(command):
    cur = ""
    # список фраз для приветствия
    answer = ["Приветствую тебя", "Рада тебя слышать", "Хай", "Здарова", "Привет", "О, привет", "Здравствуй"]

    # определяем время
    cur_time = int(datetime.datetime.now().hour)

    if 0 <= cur_time < 12:
        cur = "Доброе утро"

    if 12 <= cur_time < 18:
        cur = "Добрый день"

    if cur_time >= 18 and cur_time != 0:
        cur = "Добрый вечер"

    answer.append(cur)  # возвращаем приветствие
    answer = random.choice(answer)

    return answer
