"""
Плагин «Спасибо»

Ассистент отвечает на благодарность

"""

import random


def main(command):
    answer = random.choice(("Рада стараться", "Всегда к вашим услугам", "Пожалуйста", "Люблю, когда меня благодарят"))

    return answer
