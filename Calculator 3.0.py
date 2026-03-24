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

def convert_temp(value, mode):
    if mode == 'ctf':
        return f"Результат: {value * 1.8 + 32} F"
    elif mode == 'ftc':
        return f"Результат: {(value - 32) * 5 / 9} C"
    else:
        return "Ненайдена операция"

def convert_dist(value, mode):
    if mode == 1:
        return f"Результат: {value / 10} см"
    elif mode == 2:
        return f"Результат: {value / 1000} м"
    elif mode == 3:
        return f"Результат: {value / 1000000} км"
    elif mode == 4:
        return f"Результат: {value * 10} мм"
    elif mode == 5:
        return f"Результат: {value / 100} м"
    elif mode == 6:
        return f"Результат: {value / 100000} км"
    elif mode == 7:
        return f"Результат: {value * 1000} мм"
    elif mode == 8:
        return f"Результат: {value * 100} см"
    elif mode == 9:
        return f"Результат: {value / 1000} км"
    elif mode == 10:
        return f"Результат: {value * 1000000} мм"
    elif mode == 11:
        return f"Результат: {value * 100000} см"
    elif mode == 12:
        return f"Результат: {value * 1000} м"
    else:
        return "Ненайдена операция"    

def make_positive (value):
    if value < 0:
        return -value
    else:
        return value
    
def only_positive(value):  
    if value <= 0:
        raise ValueError 
    else:
        return value



while True:
    try:
        main_choice = input("Что вы хотите: \ncal для калькулятора \nspv для вычислений \nran для рандома \ninfo для информации \nexit для выхода\n").strip().lower()

        if main_choice == 'exit':
            print("Остановка")
            break

        elif main_choice == 'info':
            print("Версия калькулятора на языке Python\nВерсия: 3.0 \nАвтор: ShipovskijKorp\ndevblog: 20\nTg: https://t.me/+_9Ho35Hbbe8zOTEy")

        elif main_choice == 'cal':
            cal_choice = input("Выбери: \ncal для калькулятора \nurv для уравнений\ndsc для калькулятора систем счислений\nconv для конвертаций \nbmi для индекса массы тела \n").strip().lower()   

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
                x = input("Введи значение: ").upper().strip()
                input_base = int(input("Введи исходную систему счисления (2-36): "))
                output_base = int(input("Введи конечную систему счисления (2-36): "))
                print(dsc(x, input_base, output_base))

            elif cal_choice == 'conv':
                conv_mode = input("dist - конвертация дистанции \ntemp для конвертации температуры\n").strip().lower()

                if conv_mode == 'temp':
                    temp_mode = input("Выбери: ctf для C в F или ftc для F в C \n").strip().lower()
                    t = float(input("Введите температуру: "))
                    print(convert_temp(t, temp_mode))

                elif conv_mode == 'dist':
                    print("1) мм в см \n2) мм в м \n3) мм в км\n4) см в мм \n5) см в м \n6) см в км \n7) м в мм \n8) м в см \n9) м в км \n10) км в мм \n11) км в см \n12) км в м ")
                    dist_mode = int(input("Выберете операцию: "))
                    dist = float(input("Введите число: "))
                    print(convert_dist(dist, dist_mode))
                    
                else:
                    print("Ненайдена операция")

            elif cal_choice == 'bmi':
                h = float(input("Введите рост (см): "))
                m = float(input("Введите вес (кг): "))
                print(bmi(h, m))    

            else:
                print("Ненайдена операция")

        elif main_choice == 'ran':
            ran_choice = input("Выбери тип рандома: \nnum для числа \npas для пароля: ").strip().lower()

            if ran_choice == 'num':
                minN = int(input("Введите нижнюю границу: "))
                maxN = int(input("Введите верхнюю границу: "))

                if maxN < minN:
                    minN, maxN = maxN, minN
                    print(f"Возможно границы были перепутаны местами. Новые границы: от {minN} до {maxN}")
                print("Результат:", random.randint(minN, maxN))

            elif ran_choice == 'pas':
                length = int(input("Введите длину пароля, максимум 1024: "))   
                print(generate_password(length))

            else:
                print("Ненайдена операция")  

        elif main_choice == 'spv':
            print("В разработке")

        else:
            print("Ненайдена операция")      
              
    except ValueError:
        print("Ошибка ввода")

    except ZeroDivisionError:
        print("Ошибка, одно из чисел в делении равно 0")            