import math

def make_positive(value):
    if value < 0:
        return -value
    return value

def only_positive(value):
    if value <= 0:
        raise ValueError("Значение должно быть больше 0")
    return value

def triangle_check(a, b, c):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def trapezoid_check(a, b, c, d, h):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)
    d = make_positive(d)
    h = make_positive(h)

    if a == 0 or b == 0 or c == 0 or d == 0 or h == 0:
        return False
    return True

def sp():
    return "Выбери P или S"

def sl():
    return "Выбери L или S"

def sv():
    return "Выбери S или V"

def square(a, action):
    a = make_positive(a)

    if a == 0:
        return "Квадрат не существует"

    if action == "p":
        return 4 * a
    elif action == "s":
        return a * a
    else:
        return "Операция не найдена"

def rectangle(a, b, action):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Прямоугольник не существует"

    if action == "p":
        return 2 * (a + b)
    elif action == "s":
        return a * b
    else:
        return "Операция не найдена"

def paral(a, b, action):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Параллелограмм не существует"

    if action == "p":
        return 2 * (a + b)
    elif action == "s":
        return a * b
    else:
        return "Операция не найдена"

def trian_form_menu_s():
    return (
        "Выбери формулу площади треугольника:\n"
        "1) S = a*h/2\n"
        "2) S = (a*b*sin(alpha))/2\n"
        "3) S = sqrt(p*(p-a)*(p-b)*(p-c))\n"
        "4) S = (a*b*c)/(4*R)"
    )

def triangle_area_1(a, h):
    a = make_positive(a)
    h = make_positive(h)

    if a == 0 or h == 0:
        return "Треугольник не существует"

    return a * h / 2

def triangle_area_2(a, b, alpha):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Треугольник не существует"

    if alpha <= 0 or alpha >= 180:
        return "Треугольник не существует"

    return (a * b * math.sin(math.radians(alpha))) / 2

def triangle_area_3(a, b, c):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    p = (a + b + c) / 2
    expr = p * (p - a) * (p - b) * (p - c)

    if expr < 0:
        return "Такой треугольник не существует"

    return math.sqrt(expr)

def triangle_area_4(a, b, c, r):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)
    r = make_positive(r)

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    if r == 0:
        return "Такой треугольник не существует"

    return (a * b * c) / (4 * r)

def triangle_perimetr(a, b, c):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    return a + b + c

def trapezoid(a, b, c, d, h, action):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)
    d = make_positive(d)
    h = make_positive(h)

    if not trapezoid_check(a, b, c, d, h):
        return "Трапеция не существует"

    if action == "p":
        return a + b + c + d
    elif action == "s":
        return (a + b) * h / 2
    else:
        return "Операция не найдена"

def circle(r, action):
    r = make_positive(r)

    if r == 0:
        return "Круг не существует"

    if action == "l":
        return 2 * math.pi * r
    elif action == "s":
        return math.pi * r * r
    else:
        return "Операция не найдена"

def oval(a, b, action):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Овал не существует"

    if action == "s":
        return math.pi * a * b
    elif action == "l":
        return 2 * math.pi * math.sqrt((a * a + b * b) / 2)
    else:
        return "Операция не найдена"

def cube(a, action):
    a = make_positive(a)

    if a == 0:
        return "Куб не существует"

    if action == "s":
        return 6 * a * a
    elif action == "p":
        return 12 * a
    elif action == "v":
        return a ** 3
    else:
        return "Операция не найдена"

def box(a, b, c, action):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if a == 0 or b == 0 or c == 0:
        return "Параллелепипед не существует"

    if action == "s":
        return 2 * (a * b + b * c + a * c)
    elif action == "p":
        return 4 * (a + b + c)
    elif action == "v":
        return a * b * c
    else:
        return "Операция не найдена"

def sphere(r, action):
    r = make_positive(r)

    if r == 0:
        return "Сфера не существует"

    if action == "s":
        return 4 * math.pi * r * r
    elif action == "v":
        return 4 / 3 * math.pi * r ** 3
    else:
        return "Операция не найдена"

def cone(r, h, action):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Конус не существует"

    l = math.sqrt(r ** 2 + h ** 2)

    if action == "s":
        return math.pi * r * (r + l)
    elif action == "v":
        return math.pi * r * r * h / 3
    else:
        return "Операция не найдена"

def cylinder(r, h, action):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Цилиндр не существует"

    if action == "s":
        return 2 * math.pi * r * (r + h)
    elif action == "v":
        return math.pi * r * r * h
    else:
        return "Операция не найдена"