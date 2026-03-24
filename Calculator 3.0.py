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

def convert_speed(value, mode):
    if mode == 1:
        return f"Результат: {value * 3.6} км/ч"
    elif mode == 2:
        return f"Результат: {value / 3.6} м/с"
    else:
        return "Ненайдена операция"

def convert_volume(value, mode):
    if mode == 1:
        return f"Результат: {value / 1000} л"         
    elif mode == 2:
        return f"Результат: {value / 1000000} м3"     
    elif mode == 3:
        return f"Результат: {value} см3"           

    elif mode == 4:
        return f"Результат: {value * 1000} мл"      
    elif mode == 5:
        return f"Результат: {value / 1000} м3"      
    elif mode == 6:
        return f"Результат: {value * 1000} см3" 

    elif mode == 7:
        return f"Результат: {value * 1000000} мл"     
    elif mode == 8:
        return f"Результат: {value * 1000} л"    
    elif mode == 9:
        return f"Результат: {value * 1000000} см3"   

    elif mode == 10:
        return f"Результат: {value} мл"            
    elif mode == 11:
        return f"Результат: {value / 1000} л"       
    elif mode == 12:
        return f"Результат: {value / 1000000} м3"   

    else:
        return "Ненайдена операция"

def convert_mass(value, mode):
    if mode == 1:
        return f"Результат: {value / 1000} г"        
    elif mode == 2:
        return f"Результат: {value / 1000000} кг"    
    elif mode == 3:
        return f"Результат: {value / 1000000000} т"  

    elif mode == 4:
        return f"Результат: {value * 1000} мг"      
    elif mode == 5:
        return f"Результат: {value / 1000} кг"       
    elif mode == 6:
        return f"Результат: {value / 1000000} т"   

    elif mode == 7:
        return f"Результат: {value * 1000000} мг"   
    elif mode == 8:
        return f"Результат: {value * 1000} г"      
    elif mode == 9:
        return f"Результат: {value / 1000} т"       

    elif mode == 10:
        return f"Результат: {value * 1000000000} мг" 
    elif mode == 11:
        return f"Результат: {value * 1000000} г"
    elif mode == 12:
        return f"Результат: {value * 1000} кг"

    else:
        return "Ненайдена операция"

def convert_area(value, mode):
    if mode == 1:
        return f"Результат: {value / 100} см2"        
    elif mode == 2:
        return f"Результат: {value / 1000000} м2"         
    elif mode == 3:
        return f"Результат: {value / 1000000000000} км2"   

    elif mode == 4:
        return f"Результат: {value * 100} мм2"      
    elif mode == 5:
        return f"Результат: {value / 10000} м2"          
    elif mode == 6:
        return f"Результат: {value / 10000000000} км2"    

    elif mode == 7:
        return f"Результат: {value * 1000000} мм2"     
    elif mode == 8:
        return f"Результат: {value * 10000} см2"     
    elif mode == 9:
        return f"Результат: {value / 1000000} км2"     

    elif mode == 10:
        return f"Результат: {value * 1000000000000} мм2" 
    elif mode == 11:
        return f"Результат: {value * 10000000000} см2"    
    elif mode == 12:
        return f"Результат: {value * 1000000} м2"       

    else:
        return "Ненайдена операция"                  

def make_positive (value):
    if value < 0:
        return -value
    else:
        return value
    
def only_positive(value):  
    if value <= 0:
        raise ValueError("Значение должно быть больше 0")
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
                conv_mode = input("Конвертация:\ndist - дистанция \nspeed - скорость \narea - площадь\nvolume - обьем\nmass - масса\ntemp - температура\n").strip().lower()

                if conv_mode == 'temp':
                    temp_mode = input("Выбери: ctf для C в F или ftc для F в C \n").strip().lower()
                    t = float(input("Введите температуру: "))
                    print(convert_temp(t, temp_mode))

                elif conv_mode == 'dist':
                    print("1) мм в см \n2) мм в м \n3) мм в км\n4) см в мм \n5) см в м \n6) см в км \n7) м в мм \n8) м в см \n9) м в км \n10) км в мм \n11) км в см \n12) км в м ")
                    dist_mode = int(input("Выберете операцию: "))
                    dist = float(input("Введите значение: "))
                    print(convert_dist(dist, dist_mode))

                elif conv_mode == 'speed':
                    print("1) м/с в км/ч \n2) км/ч в м/с")
                    speed_mode = int(input("Выберете операцию: "))
                    speed = float(input("Введите значение: "))
                    print(convert_speed(speed, speed_mode))

                elif conv_mode == 'volume':
                    print("1) мл в л\n2) мл в м3\n3) мл в см3\n4) л в мл\n5) л в м3\n6) л в см3\n7) м3 в мл\n8) м3 в л\n9) м3 в см3\n10) см3 в мл\n11) см3 в л\n12) см3 в м3")
                    mode = int(input("Выберете операцию: "))
                    value = float(input("Введите объем: "))
                    print(convert_volume(value, mode))

                elif conv_mode == 'mass':
                    print("1) мг в г\n""2) мг в кг\n""3) мг в т\n""4) г в мг\n""5) г в кг\n""6) г в т\n""7) кг в мг\n""8) кг в г\n""9) кг в т\n""10) т в мг\n""11) т в г\n""12) т в кг")
                    mode = int(input("Выберите операцию: "))
                    value = float(input("Введите массу: "))
                    print(convert_mass(value, mode))

                elif conv_mode == 'area':
                    print("1) мм2 в см2\n2) мм2 в м2\n3) мм2 в км2\n4) см2 в мм2\n5) см2 в м2\n6) см2 в км2\n7) м2 в мм2\n8) м2 в см2\n9) м2 в км2\n10) км2 в мм2\n11) км2 в см2\n12) км2 в м2")
                    mode = int(input("Выберете операцию: "))
                    value = float(input("Введите площадь: "))
                    print(convert_area(value, mode))

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