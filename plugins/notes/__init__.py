"""
Плагин «Заметки»

Ассистент сохраняет текстовую заметку в файл notes.txt. Может показать содержимое этого файла и очистить его
"""

__author__ = 'rad-li'
__version__ = 0.2


add = ("запиши", "сохрани", "добавь", "заметка")
show = ("покажи", "прочитай", "открой")
delete = ("очисти", "удали")


def main(command):
    answer = ""
    # command = command.replace("в заметки", "")
    # command = command.replace("заметку", "")
    # command = command.replace("заметки", "")
    command = command.replace("  ", "")

    for i in add:
        if i in command:

            try:
                notes_content = command.replace(i, "")

                notes = open("notes.txt", "a")
                notes.write(notes_content + "\n")
                notes.close()
                answer = "Записала " + notes_content
            except Exception:
                notes_content = command.replace(i, "")
                notes = open("notes.txt", "w")
                notes.write(notes_content + "\n")
                notes.close()
                answer = "Записала " + notes_content
            break

    for i in show:
        if i in command:

            notes = open("notes.txt", "r")
            notes_content = notes.read()

            if notes_content:
                notes = open("notes.txt", "r")
                answer = "Ваши заметки:\n"
                for item in notes:
                    item = item.replace(" и ", "\n").replace(",", "\n")
                    answer += item

                notes.close()

            else:
                answer = "Список заметок пуст"
                break

    for i in delete:
        if i in command:
            notes = open("notes.txt", "w")
            notes.write("")
            notes.close()
            answer = "Заметки очищены"
            break

    return answer
