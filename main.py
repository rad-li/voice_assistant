""" Голосовой ассистент """

__author__ = 'rad-li'
__version__ = 0.3


import speech_recognition
import subprocess
import plugin_loader
import stt
import gstt

# Создание объекта Recognizer
sr = speech_recognition.Recognizer()
# Установка порога простоя для остановки записи
sr.pause_threshold = 0.5


def replace_non_alphanumeric(string):
    """Функция удаляет все не буквенные и не числовые значения из строки, кроме пробела"""

    result = ''
    for char in string:
        if not char.isalnum() and char != ' ':
            result += ''
        else:
            result += char
    return result


def listen_command():

    """ Функция вызывает модуль распознавания речи и возвращает распознанный текст"""

    # здесь можно выбрать офлайн или онлайн распознавание
    # text = stt.main()  # офлайн распознавание с помощью vosk
    text = gstt.main() # онлайн распознавание с помощью google

    if text != "":
        return text

    # если закомментировать предыдущие строки кода и раскомментировать строку 44,
    # общение с ассистентом будет происходить в текстовом режиме
    # return ' '.join(input().lower().split())


def say_message(message):
    """Печатает и озвучивает ответ"""

    print(message)
    subprocess.run(["mplayer", "-really-quiet", "-nolirc",
                    'http://tts.voicetech.yandex.net/tts?format=mp3&quality=hi&lang=ru_RU&text='+message])

if __name__ == "__main__":

    # запускаем бесконечный цикл
    # слушаем команды пользователя
    while True:

        # команда пользователя
        command = listen_command().lower()
        # print(command)

        if command is not None:
            say_message(plugin_loader.main(replace_non_alphanumeric(command)))
