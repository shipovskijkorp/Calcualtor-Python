import math
import random
import secrets
import string

def generate_password(length, config):
    max_length = config["password"]["max_length"]

    if length < 0:
        length = -length
        message = "Отрицательная длина не поддерживается, введенное значение преобразовано в положительное\n"
    else:
        message = ""

    if length == 0:
        return "Пароль с длиной 0 недоступен"

    if length > max_length:
        length = max_length
        message += f"Длина пароля ограничена {max_length} символами, длина пароля обрезана до {max_length}\n"

    characters = string.ascii_letters + string.digits
    password = "".join(secrets.choice(characters) for _ in range(length))

    return f"{message}Твой пароль: {password}"

def random_number(min_value, max_value):
    if max_value < min_value:
        min_value, max_value = max_value, min_value
        print(f"Возможно границы были перепутаны местами. Новые границы: от {min_value} до {max_value}")

    return random.randint(min_value, max_value)

def urv(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                result = "Бесконечно много решений"
            else:
                result = "Нет решений"
        else:
            x = -c / b
            x = round(x, 2)
            result = f"x = {x}"
    else:
        d = b ** 2 - 4 * a * c

        if d < 0:
            result = "Нет корней"
        elif d == 0:
            x = (-b) / (2 * a)
            x = round(x, 2)
            result = f"x = {x}"
        else:
            x1 = ((-b) + math.sqrt(d)) / (2 * a)
            x1 = round(x1, 2)
            x2 = ((-b) - math.sqrt(d)) / (2 * a)
            x2 = round(x2, 2)
            result = f"x1 = {x1}\nx2 = {x2}"

    return result

def dsc(x, input_base, output_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dscresult = ""

    if input_base < 2 or input_base > 36 or output_base < 2 or output_base > 36:
        return "Такой системы счисления не существует"

    try:
        a = int(x, input_base)
    except ValueError:
        return "Некорректное число для указанной системы счисления"

    if a == 0:
        dscresult = "0"
    else:
        sign = ""
        if a < 0:
            sign = "-"
            a = -a

        while a > 0:
            dscresult = digits[a % output_base] + dscresult
            a = a // output_base

        dscresult = sign + dscresult

    return f"Ответ: {dscresult}"

def bmi(height, weight):
    message = ""

    if height == 0:
        return "Рост не может быть равен 0!"

    if height < 0:
        height = -height
        message += "Рост не может быть отрицательным, отрицательное значение конвертировано в положительное\n"

    if height < 140:
        message += "Хоббиты общий сбор!!!\n"

    if weight == 0:
        return "Вес не может быть равен 0!"

    if weight < 0:
        weight = -weight
        message += "Вес не может быть отрицательным, отрицательное значение конвертировано в положительное\n"

    height_m = height / 100
    index = weight / (height_m * height_m)

    return f"{message}Результат: {round(index, 1)}"

def calculator_main_function(expr):
    expr = expr.replace("^", "**")
    allowed = "0123456789+-*/(). %"

    if not all(ch in allowed for ch in expr):
        return "Недопустимые символы"

    result = eval(expr, {"__builtins__": None}, {})
    return f"Результат: {result}"