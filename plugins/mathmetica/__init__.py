"""
Плагин «Математика»

Ассистент считает простые математические выражения на сложение, вычитание, умножение и деление.
Если плагин получает числа в текстовом формате (например, "пять", вместо "5"), они будут преобразованы
с помощью модуля ru_word2number
"""

from ru_word2number import w2n


trigger = 'посчитай, сколько будет, результат выражения, математика, матика'

# математические знаки
math_symbols = ("+", "-", "*", "/")

# словарь соотвествия математичсеких знаков ил словесному описанию
math_words = {"плюс": "+", "прибавить": "+", "сложить": "+", "минус": "-", "вычесть": "-", "умножить": "*", "разделить": "/"}


def get_nums(expression):
    # обнуляем переменную
    expression_to_nums = ""

    # создаем список и проверяем каждое слово
    for word in expression.split():
        try:
            # если слово - число в строковом виде, преобразуем его в цифровой вид
            num = w2n.word_to_num(word)

            # добавляем его в переменную
            expression_to_nums += f" {str(num)}"
        except ValueError:
            # если слово не число, добавляем его в переменную как есть
            expression_to_nums += f" {word}"

    # возвращаем строку, где все числа преобразованы в цифровой вид
    return expression_to_nums


def clear(expression):
    # обнуляем переменную
    cleaned_expression = ""

    # создаем список и проверяем каждое слово на число
    # и по списку mathSymbols на вхождение математических знаков
    for word in expression.split():

        # если это число или мат. знаков
        if word.isdigit() or word in math_symbols:

            # записываем его в переменную
            cleaned_expression += word

        # проверяем по словарю math_words на вхождение математических знаков
        elif word in math_words:

            # получаем математический знак по слову
            word = math_words.get(word)
            cleaned_expression += word

    # возвращаем математическое выражение очищенное от лишних слов
    return cleaned_expression


def main(command):
    answer = ""
    for i in trigger:
        if i in command:
            nums = get_nums(command)
            cleaned = clear(nums)
            try:
                answer = str(eval(cleaned))  # Счёт выражения
            except Exception:
                answer = "Не удалось посчитать выражение."
            break
        else:
            answer = "Математика тут бессильна"

    # возвращаем ответ математического выражения
    return answer
