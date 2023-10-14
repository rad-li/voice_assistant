"""
Голосовой ассистент

rad-li@ya.ru
v. 0.1
"""
__author__ = 'rad-li'
__version__ = 0.1


import os
import subprocess   # для запуска внешних программ
import signal       # прерывание по нажатию ctrl+c
import requests     # для сетевых запросов
import datetime     # для работы с датой и временем


# настройки погоды
city = ""           # указываем город
appid = ""          # api-ключ openweathermap


# отправляем запрос на сервер, получаем результат в json-формате
weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                            + city + "&units=metric&lang=ru&appid=" + appid).json()
temp = round(weather_data["main"]["temp"])                  # получаем данные о температуре


# данные ассистента
name = "Пятница"                                            # имя ассистента
bio = "Я - " + name + " - голосовой помощник"               # кто он такой
age = "21 августа 2023 года"                                # дата создания (день рождения)
skill = "Я умею отвечать на вопросы, делать заметки, " \
        "считать как калькулятор, запускать программы " \
        "на компьютере сообщать погоду, дату и время"       # навыки ассистента


# названия программ и строки их запуска
program_name = ["калькулятор", "гимп", "блендер", "файлы", "телеграм", "терминал"]
program_exec = ["kcalc", "gimp", "blender", "dolphin", "telegram-desktop", "konsole"]


def listen_command():
    """ Принимает строку от пользователя и возвращает ее в нижнем регистре """

    return input().lower()


# приветствие в зависимости от времени суток
def greet():
    """ Возвращает строку с приветствием в зависимости от времени суток """

    current_hour = int(datetime.datetime.now().hour)  # определяем текущий час
    cur = "Привет"
    if 0 <= current_hour < 12:
        cur = "Доброе утро"

    if 12 <= current_hour < 18:
        cur = "Добрый день"

    if current_hour >= 18 and current_hour != 0:
        cur = "Добрый вечер"
    return cur  # возвращаем приветствие


def log_wrong_command(command):
    """
    Записывает в файл строку с неопознанной командой

    Если файл не существует, он будет создан

    Параметры
    ---------
    command : str
            команда
    """

    with open("wrong_command.txt", "a") as wrong:
        wrong.writelines(command + "\n")


def say_message(command):
    """
    Печатает и озвучивает ответ

    Текст команды отправляется на сервер распознавания Яндекса,
    полученный аудиофайл передается в mplayer для проигрывания

    Параметры
    ---------
    command : str
            команда
    """

    print(command)
    subprocess.run(["mplayer", "-really-quiet", "-nolirc",
                    'http://tts.voicetech.yandex.net/tts?format=mp3&quality=hi&lang=ru_RU&text='+command])


# завершение программы по ctrl+c
def handle_interrupt(signal, frame):
    """ Отлавливает нажатие комбинации клавиш CTRL+ C"""

    print("Отключаюсь")
    exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


# выполняем команду
def do_this_command(command):
    """
    Выполняет команду

    В зависимости от совпадения выполняет ту или иную команду

    Параметры
    ---------
    command : str
            команда полученная с функцией listen_command()
    """

    if "привет" in command:
        say_message(greet())

    elif "зовут" in command:
        say_message("Меня зовут " + name)

    elif "кто ты" in command:
        say_message(bio)

    elif "что ты умеешь" in command:
        say_message(skill)

    elif "сколько тебе лет" in command:
        say_message("Меня создали " + age)

    elif "как дел" in command:
        say_message("Хорошо. Все системы работают в штатном режиме")

    elif "время" in command or "час" in command:
        say_message(str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))

    elif "сегодня день" in command:
        say_message(datetime.datetime.now().strftime("%d.%m.%Y"))

    elif "пока" in command:
        say_message("Пока")
        exit(0)

    elif "запусти" in command or "открой" in command:
        command = command.split()
        say_message("запускаю " + command[1])
        exec_num = program_name.index(command[1])
        os.system(program_exec[exec_num])

    elif "сохрани" in command or "запомни" in command or "заметк" in command or "запиши" in command:
        command = command.split()
        wr = ' '.join(command[1:len(command)+1])
        with open("todo.txt", "a") as f:
            f.writelines(wr + "\n")
        say_message("записала " + wr)

    elif "погод" in command:
        say_message("Сейчас в городе " + str(temp) + " °C")

    else:
        say_message("Команда не распознана")
        log_wrong_command(command)


if __name__ == "__main__":

    while True:
        command = listen_command()  # считываем текстовую команду
        do_this_command(command)    # выполняем команду
