import math

def make_positive(value):
    if value < 0:
        return -value
    return value

def only_positive(value):
    if value <= 0:
        raise ValueError("Значение должно быть больше 0")
    return value

def sp():
    return "Выбери P или S"

def sl():
    return "Выбери L или S"

def spv():
    return "Выбери S, P или V"

def square(a, action):
    a = make_positive(a)

    if action == "p":
        return 4 * a
    elif action == "s":
        return a * a

def rectangle(a, b, action):
    a = make_positive(a)
    b = make_positive(b)

    if action == "p":
        return 2 * (a + b)
    elif action == "s":
        return a * b

def paral(a, b, action):
    a = make_positive(a)
    b = make_positive(b)

    if action == "p":
        return 2 * (a + b)
    elif action == "s":
        return a * b

def trian_form_menu():
    return (
        "Выбери формулу площади треугольника:\n"
        "1) S = a*h/2\n"
        "2) S = (a*b*sin(alpha))/2\n"
        "3) S = sqrt(p*(p-a)*(p-b)*(p-c))\n"
        "4) S = (a*b*c)/(4*R)"
    )

def triangle_area(choice):
    if choice == "1":
        a = float(input("Введите сторону a: "))
        h = float(input("Введите высоту h: "))
        return a * h / 2

    elif choice == "2":
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        alpha = float(input("Введите угол alpha в градусах: "))
        return (a * b * math.sin(math.radians(alpha))) / 2

    elif choice == "3":
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    elif choice == "4":
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        R = float(input("Введите радиус описанной окружности R: "))
        return (a * b * c) / (4 * R)

    else:
        return "Формула не найдена"  

def triangle_perimetr(a, b, c):
    return a+b+c    