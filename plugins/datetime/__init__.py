"""
Плагин «Дата и время»

Ассистент сообщает время, дату, месяц, год и дату с временем
"""

__author__ = 'rad-li'
__version__ = 0.2


import datetime
import locale


locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


time = 'который час, подскажи время, сколько время, сколько времени, сколько сейчас время, подскажи время, время'
day = 'который день, какой день, какой сегодня день, какой сейчас день'
month = 'какой месяц, какой сегодня месяц, какой сейчас месяц,'
date = 'который год, какой год, какой сегодня год, какой сейчас год'

now = datetime.datetime.now()  # Получение текущей даты
months = {"01": "январь",
          "02": "февраль",
          "03": "март",
          "04": "апрель",
          "05": "май",
          "06": "июнь",
          "07": "июль",
          "08": "август",
          "09": "сентябрь",
          "10": "октябрь",
          "11": "ноябрь",
          "12": "декабрь"}


def main(command):
    if command in day:
        answer = f"Сегодня {now.strftime('%d')} {now.strftime('%B')}"
    elif command in month:
        answer = f"Сейчас {months[now.strftime('%m')]}"
    elif command in date:
        answer = f"Сейчас {now.strftime('%Y')} год"
    elif command in time:
        answer = now.strftime("%H:%M")
    else:
        answer = f"Сегодня {now.strftime('%d')} {now.strftime('%B')} {now.strftime('%Y')} года, {now.strftime('%H:%M')}"

    return answer
