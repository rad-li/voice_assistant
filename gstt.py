""" Запись аудио с помощью микрофона и распознавание речи с использованием библиотеки speech_recognition """

__author__ = 'rad-li'
__version__ = 0.3


# импортируем библиотеку speech_recognition и назовем ее как `sr`, чтобы обращаться к ее функциям и классам
import speech_recognition as sr


def main():
    """ Функции записывает и распознает речь """

    # Создаем экземпляр класса Recognizer из библиотеки speech_recognition
    # Этот класс предоставляет функции для распознавания речи
    r = sr.Recognizer()

    # Cоздаем объект Microphone и назначаем его source.
    # device_index указывает индекс устройства записи звука, в данном случае 4.
    # Можно измененить в зависимости от конфигурации аудиоустройств компьютера.
    with sr.Microphone(device_index=4) as source:

        # Настройка для удаления посторонних шумов. duration указывает время в секундах,
        # в течение которого алгоритм будет слушать фоновые шумы для настройки
        r.adjust_for_ambient_noise(source, duration=0.5)

        # Запись аудио с помощью микрофона и сохранение его в переменную audio
        audio = r.listen(source)

        # С помощью функции recognize_google из объекта r распознаем речь из переменной audio.
        # Речь распознается с использованием сервиса Google Speech Recognition.
        # Параметр language указывает на язык речи, в данном случае русский
        text = r.recognize_google(audio, language='ru-RU')

        if text != "":
            print(text)

    return text
