""" Голосовой ассистент """

__author__ = 'rad-li'
__version__ = 0.2

import subprocess
# import speech_recognition
# import sounddevice
import plugin_loader


# Создание объекта Recognizer
# sr = speech_recognition.Recognizer()
# Установка порога простоя для остановки записи
# sr.pause_threshold = 0.5


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
    # """Функция распознает голосовую команду и возвращает текстовую строку"""
    #
    # try:
    #     with speech_recognition.Microphone() as mic:
    #         sr.adjust_for_ambient_noise(source=mic, duration=0.9) # удаление посторонних шумов
    #         audio = sr.listen(source=mic)
    #         query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    #
    #     return query
    #
    # except speech_recognition.UnknownValueError:
    #     pass

    """Принимает строку от пользователя и возвращает ее в нижнем регистре"""
    return ' '.join(input().lower().split())


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
        command = listen_command()

        if command is not None:
            say_message(plugin_loader.main(replace_non_alphanumeric(command)))
