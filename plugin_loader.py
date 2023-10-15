"""Загрузчик плагинов"""

__author__ = 'rad-li'
__version__ = 0.2

import importlib
import glob
import os


def get_plugins_dirs():
    """Функция возвращает список абсолютных путей к папкам плагинов"""

    # получаем абсолютные пути файлов в папке plugins
    plugin_pathnames = glob.glob(os.path.abspath('plugins') + '/*/')
    plugin_dirs = []

    # в цикле заносим в список пути к папкам, внутри которых есть файл __init__.py, кроме папки __pycache__
    for plugin_dir in plugin_pathnames:

        if os.path.isdir(plugin_dir) \
                and ("__init__.py" in os.listdir(plugin_dir))\
                and ("__pycache__" not in plugin_dir):
            # записываем пути в список без правого слешка
            plugin_dirs.append(plugin_dir.rstrip('/'))

    # возвращаем список абсолютных путей к папкам плагинов
    return plugin_dirs


def get_plugins_names():
    """Функция получает названия папок плагинов"""

    path = "plugins"  # папка в плагинами
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and f != "__pycache__"]

    return folders


def get_triggers():
    """Функция собирает триггеры со всех плагинов и соотносит их с назвнием плагина"""

    triggers = {}

    for name in get_plugins_names():

        for filename in os.listdir('plugins/' + name):
            file_path = os.path.join('plugins/' + name, filename)

            content = []  # список для хранения содержимого файлов

            # проверяем, является ли объект файлом и имеет ли расширение .trigger
            if os.path.isfile(file_path) and filename.endswith('.trigger'):

                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    content.extend([line.strip() for line in lines])
                    triggers[name] = content

    return triggers


def find_key(dictionary, value):
    """Функция для нахождения ключа в словаре по значению"""

    for k, v in dictionary.items():
        if value in v:
            return k
    # если значение не будет найдено, функция вернет None
    return None


def check_values(dictionary, string):
    for key, values in dictionary.items():
        for value in values:
            if value in string:
                return key
    return None



def load_plugin(plugin_name, command):
    """
    Функция для импорта плагина как модуля питона

    Параметры
    ---------
    plugin : str
            название плагина для импорта
    command : str
            команда для выполнения плагином
    """

    my_plugin = importlib.import_module('plugins.' + plugin_name + '.__init__')
    run = my_plugin.main(command)  # вызов функции main из импортированного модуля
    return run

def main(command):
    triggers = get_triggers()


    # plugin_name = find_key(triggers, command)
    plugin_name = check_values(triggers, command)

    if plugin_name:
        run = load_plugin(plugin_name, command)

    else:
        with open("wrong_command.txt", "a") as wrong:
            wrong.writelines(command + "\n")
        run = "Запрос не найден"
    return run