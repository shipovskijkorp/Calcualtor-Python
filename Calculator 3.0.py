import math
import secrets
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

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
            result = f"x1 = {x1}, x2 = {x2}"
    return result   

def dsc(x, input_base, output_base):

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dscresult = ""

    if input_base < 2 or input_base > 36 or output_base < 2 or output_base > 36:
        return "такой системы счисления не существует"
    else:
        a = int(x, input_base)

        if a == 0:
            dscresult = "0"
        else:
            while a > 0:
                dscresult = digits[a % output_base] + dscresult
                a = a // output_base
    result = f"Ответ:  {dscresult}"
    return result        
