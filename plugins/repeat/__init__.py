"""
Плагин «Повторитель»

Ассистент повторяет фразу сказанную пользователем

"""

__author__ = 'rad-li'
__version__ = 0.2

trigger = ('повтори', 'повторяй', 'повтори за мной')


def main(command):
    answer = ""
    for i in trigger:
        if i in command:

            answer = command.replace(i, "")
            answer = answer.replace(" за мной", "")
            break
        else:
            answer = ""

    return answer.strip()
