import math
import secrets
import random
import string

def generate_password(length):
    if length < 0:
        length = -length
        message = "Отрицательная длина не поддерживается, введенное значение преобразовано в положительное\n"
    else:
        message = ""

    if length == 0:
        return "Пароль с длиной 0 недоступен"

    if length > 1024:
        length = 1024
        message += "Длина пароля ограничена 1024 символами, длина пароля обрезана до 1024\n"

    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return f"{message}Твой пароль: {password}"

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
        d = b**2 - 4*a*c

        if d < 0:
            result = "Нет корней"       
        elif d == 0:
            x = (-b) / (2 * a)
            x = round(x, 2)
            result = f"x = {x}"
        else:
            x1 = ((-b) + math.sqrt(d)) / (2*a)
            x1 = round(x1, 2)
            x2 = ((-b) - math.sqrt(d)) / (2*a)
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

    result = f"Ответ: {dscresult}"
    return result

while True:
    try:
        main_choice = input("Что вы хотите: \ncal для калькулятора \nspv для вычислений \nran для рандома \ndop для дополнительных функций \ninfo для информации \nexit для выхода\n").strip().lower()

        if main_choice == 'exit':
            print("Остановка")
            break

        elif main_choice == 'info':
            print("Версия калькулятора на языке Python\nВерсия: 3.0 \nАвтор: ShipovskijKorp\ndevblog: 20\nTg: https://t.me/+_9Ho35Hbbe8zOTEy")

        elif main_choice == 'cal':
            cal_choice = input("Выбери: \ncal для калькулятора \nurv для уравнений\ndsc для калькулятора систем счислений\n").strip().lower()   

            if cal_choice == 'cal':
                expr = input("Введи выражение: ")
                expr = expr.replace("^", "**")
                result = eval(expr)
                print("Результат:", result) 

            elif cal_choice == 'urv':
                a = int(input("Введите коэффициент x^2: "))
                b = int(input("Введите коэффициент x: "))
                c = int(input("Введите свободный член: "))
                print(urv(a, b, c))

            elif cal_choice == 'dsc':
                x = input("Введи значение: ").upper()
                input_base = int(input("Введи исходную систему счисления (2-36): "))
                output_base = int(input("Введи конечную систему счисления (2-36): "))
                print(dsc(x, input_base, output_base))

            else:
                print("Ненайдена операция")

        elif main_choice == 'ran':
            ran_choice = input("Выбери тип рандома: \nnum для числа \npas для пароля: ").strip().lower()

            if ran_choice == 'num':
                minN = int(input("Введите нижнюю границу: "))
                maxN = int(input("Введите верхнюю границу: "))
                if maxN < minN:
                    minN, maxN = maxN, minN
                    print(f"Значения недопустимы, верхняя граница не может быть меньше нижней. Новые границы: от {minN} до {maxN}")
                print("Результат:", random.randint(minN, maxN))

            elif ran_choice == 'pas':
                length = int(input("Введите длину пароля, максимум 1024: "))   
                print(generate_password(length))

            else:
                print("Ненайдена операция")  

        else:
            print("Ненайдена операция")      
              
    except ValueError:
        print("Ошибка ввода")

    except ZeroDivisionError:
        print("Ошибка, одно из чисел в делении равно 0")            