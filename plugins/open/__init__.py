"""
Плагин «Программы и сайты»

Ассистент запускает запрошенную пограмму на компьютере или открывает запрошенный сайт.
Спсиок разрешенных программ можно изменить в `program_list`
Спсиок разрешенных сайтов можно изменить в `url_list`
"""

__author__ = 'rad-li'
__version__ = 0.2


import webbrowser
import subprocess


# названия программ и строки их запуска
program_list = {"kcalc": ["калькулятор"],
                "gimp": ["гимп", "gimp"],
                "firefox": ["браузер", "интенет"],
                "blender": ["блендер", "blender"],
                "dolphin": ["файлы", "файловый менеджер"],
                "konsole": ["терминал", "командную строку"],
                "telegram-desktop": ["телеграм", "телегу", "telegram"],
                "libreoffice": ["офис", "ворд", "эксель"]}

url_list = {"https://youtube.com/": ["youtube", "ютуб", "ютьюб", "ютюб"],
            "https://ya.ru/": ["яндекс", "yandex", "поиск"],
            "https://google.com/": ["google", "гугл", "гугль"],
            "https://github.com/": ["github", "гитхаб", "гит"]}


def main(command):
    answer = ""
    command = command.replace("открой", "")
    command = command.replace("запусти", "")

    for key, values in program_list.items():
        for value in values:
            if value in command:
                answer = "Запускаю " + key
                subprocess.Popen(key)

    for key, values in url_list.items():
        for value in values:
            if value in command:
                answer = "Открываю " + command
                webbrowser.open_new_tab(key)

    return answer
