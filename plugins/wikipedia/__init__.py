"""
Плагин «Википедиа»

Ассистент по запросу пользователя ищет статью на Википедии и выводит первые 4 предложения
"""

__author__ = 'rad-li'
__version__ = 0.2

import wikipedia


trigger = ("что такое", "кто такой", "кто такая", "кто такие")

wikipedia.set_lang("ru")  # Установка русского языка для Википедии


def main(command):
    answer = ""
    for i in trigger:
        if i in command:
            question = command.replace(i, " ")

            if question == "" or question == " " or question == "  ":
                answer = "Задан пустой запрос"
            else:
                sentencesCount = 4
                if sentencesCount > 0:

                    # Получение первых sentencesCount предложений из статьи, соответствующей запросу
                    answer = wikipedia.summary(question, sentences=sentencesCount)

                else:
                    answer = "Я такого не знаю."

    return answer
