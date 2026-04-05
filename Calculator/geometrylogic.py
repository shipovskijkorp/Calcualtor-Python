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

    if a == 0 and b == 0 and c == 0 and d == 0 and h == 0:
        return False
    return True



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

def square_diagonal(a):
    a = make_positive(a)

    if a == 0:
        return "Квадрат не существует"

    return a * math.sqrt(2)

def square_side_from_diagonal(d):
    d = make_positive(d)

    if d == 0:
        return "Квадрат не существует"

    return d / math.sqrt(2)

def square_area_from_diagonal(d):
    d = make_positive(d)

    if d == 0:
        return "Квадрат не существует"

    return d * d / 2

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

def rectangle_diagonal(a, b):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Прямоугольник не существует"

    return math.sqrt(a * a + b * b)

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

def paral_area_angle(a, b, alpha):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Параллелограмм не существует"

    if alpha <= 0 or alpha >= 180:
        return "Параллелограмм не существует"

    return a * b * math.sin(math.radians(alpha))

def paral_diagonal_1(a, b, alpha):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Параллелограмм не существует"

    if alpha <= 0 or alpha >= 180:
        return "Параллелограмм не существует"

    return math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(alpha)))

def paral_diagonal_2(a, b, alpha):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Параллелограмм не существует"

    if alpha <= 0 or alpha >= 180:
        return "Параллелограмм не существует"

    return math.sqrt(a * a + b * b + 2 * a * b * math.cos(math.radians(alpha)))

def trian_form_menu_s():
    return (
        "Выбери формулу площади треугольника:\n"
        "1) S = a*h/2\n"
        "2) S = (a*b*sin(alpha))/2\n"
        "3) S = sqrt(p*(p-a)*(p-b)*(p-c))\n"
        "4) S = (a*b*c)/(4*R)\n"
        "5) S = p*r\n"
        "6) S = c*h_c/2\n"
        "7) S = a*b/2"
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

def triangle_area_5(a, b, c, r):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)
    r = make_positive(r)

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    if r == 0:
        return "Такой треугольник не существует"

    p = (a + b + c) / 2
    return p * r

def triangle_area_6(c, h):
    c = make_positive(c)
    h = make_positive(h)

    if c == 0 or h == 0:
        return "Треугольник не существует"

    return c * h / 2

def triangle_area_7(a, b):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Треугольник не существует"

    return a * b / 2

def triangle_perimetr(a, b, c):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    return a + b + c

def triangle_half_perimetr(a, b, c):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    return (a + b + c) / 2

def triangle_height_from_area(s, a):
    s = make_positive(s)
    a = make_positive(a)

    if s == 0 or a == 0:
        return "Треугольник не существует"

    return 2 * s / a

def triangle_inradius(s, a, b, c):
    s = make_positive(s)
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if s == 0:
        return "Треугольник не существует"

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    p = (a + b + c) / 2
    return s / p

def triangle_circumradius(s, a, b, c):
    s = make_positive(s)
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if s == 0:
        return "Треугольник не существует"

    if not triangle_check(a, b, c):
        return "Такой треугольник не существует"

    return (a * b * c) / (4 * s)

def right_triangle_hypotenuse(a, b):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Треугольник не существует"

    return math.sqrt(a * a + b * b)

def right_triangle_leg(c, b):
    c = make_positive(c)
    b = make_positive(b)

    if c == 0 or b == 0:
        return "Треугольник не существует"

    if b >= c:
        return "Треугольник не существует"

    return math.sqrt(c * c - b * b)

def trian_form_menu_l():
    return (
        "Выбери формулу длины окружности:\n"
        "1) L = 2*pi*r\n"
        "2) L = pi*d"
    )

def circle_length_1(r):
    r = make_positive(r)

    if r == 0:
        return "Круг не существует"

    return 2 * math.pi * r

def circle_length_2(d):
    d = make_positive(d)

    if d == 0:
        return "Круг не существует"

    return math.pi * d

def circle_area_menu():
    return (
        "Выбери формулу площади круга:\n"
        "1) S = pi*r^2\n"
        "2) S = pi*d^2/4\n"
        "3) S = L^2/(4*pi)"
    )

def circle_area_1(r):
    r = make_positive(r)

    if r == 0:
        return "Круг не существует"

    return math.pi * r * r

def circle_area_2(d):
    d = make_positive(d)

    if d == 0:
        return "Круг не существует"

    return math.pi * d * d / 4

def circle_area_3(l):
    l = make_positive(l)

    if l == 0:
        return "Круг не существует"

    return l * l / (4 * math.pi)

def circle_radius_from_diameter(d):
    d = make_positive(d)

    if d == 0:
        return "Круг не существует"

    return d / 2

def circle_diameter_from_radius(r):
    r = make_positive(r)

    if r == 0:
        return "Круг не существует"

    return 2 * r

def circle_radius_from_length(l):
    l = make_positive(l)

    if l == 0:
        return "Круг не существует"

    return l / (2 * math.pi)

def trapezoid_form_menu_s():
    return (
        "Выбери формулу площади трапеции:\n"
        "1) S = (a+b)*h/2\n"
        "2) S = m*h"
    )

def trapezoid_area_1(a, b, h):
    a = make_positive(a)
    b = make_positive(b)
    h = make_positive(h)

    if a == 0 or b == 0 or h == 0:
        return "Трапеция не существует"

    return (a + b) * h / 2

def trapezoid_area_2(m, h):
    m = make_positive(m)
    h = make_positive(h)

    if m == 0 or h == 0:
        return "Трапеция не существует"

    return m * h

def trapezoid_perimetr(a, b, c, d):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)
    d = make_positive(d)

    if a == 0 or b == 0 or c == 0 or d == 0:
        return "Трапеция не существует"

    return a + b + c + d

def trapezoid_middle_line(a, b):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Трапеция не существует"

    return (a + b) / 2

def trapezoid_height_from_area(s, a, b):
    s = make_positive(s)
    a = make_positive(a)
    b = make_positive(b)

    if s == 0 or a == 0 or b == 0:
        return "Трапеция не существует"

    return 2 * s / (a + b)

def trapezoid_equal_side(a, b, h):
    a = make_positive(a)
    b = make_positive(b)
    h = make_positive(h)

    if a == 0 or b == 0 or h == 0:
        return "Трапеция не существует"

    return math.sqrt(h * h + ((a - b) / 2) ** 2)

def trapezoid(a, b, c, d, h, action):
    if action == "p":
        return trapezoid_perimetr(a, b, c, d)
    elif action == "s":
        return trapezoid_area_1(a, b, h)
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

def oval_length_2(a, b):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Овал не существует"

    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

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

def cube_face_diagonal(a):
    a = make_positive(a)

    if a == 0:
        return "Куб не существует"

    return a * math.sqrt(2)

def cube_diagonal(a):
    a = make_positive(a)

    if a == 0:
        return "Куб не существует"

    return a * math.sqrt(3)

def cube_side_area(a):
    a = make_positive(a)

    if a == 0:
        return "Куб не существует"

    return 4 * a * a

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

def box_diagonal(a, b, c):
    a = make_positive(a)
    b = make_positive(b)
    c = make_positive(c)

    if a == 0 or b == 0 or c == 0:
        return "Параллелепипед не существует"

    return math.sqrt(a * a + b * b + c * c)

def box_base_area(a, b):
    a = make_positive(a)
    b = make_positive(b)

    if a == 0 or b == 0:
        return "Параллелепипед не существует"

    return a * b

def sphere_form_menu():
    return (
        "Выбери формулу сферы:\n"
        "1) S = 4*pi*r^2\n"
        "2) V = 4*pi*r^3/3\n"
        "3) V = pi*d^3/6\n"
        "4) S = pi*d^2"
    )

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

def sphere_volume_d(d):
    d = make_positive(d)

    if d == 0:
        return "Сфера не существует"

    return math.pi * d ** 3 / 6

def sphere_area_d(d):
    d = make_positive(d)

    if d == 0:
        return "Сфера не существует"

    return math.pi * d * d

def sphere_radius_from_diameter(d):
    d = make_positive(d)

    if d == 0:
        return "Сфера не существует"

    return d / 2

def sphere_diameter_from_radius(r):
    r = make_positive(r)

    if r == 0:
        return "Сфера не существует"

    return 2 * r

def cone_form_menu():
    return (
        "Выбери формулу конуса:\n"
        "1) S = pi*r*(r+l)\n"
        "2) S бок = pi*r*l\n"
        "3) V = pi*r^2*h/3\n"
        "4) l = sqrt(r^2+h^2)\n"
        "5) S осн = pi*r^2"
    )

def cone_area_full(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Конус не существует"

    l = math.sqrt(r ** 2 + h ** 2)
    return math.pi * r * (r + l)

def cone_area_side(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Конус не существует"

    l = math.sqrt(r ** 2 + h ** 2)
    return math.pi * r * l

def cone_volume(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Конус не существует"

    return math.pi * r * r * h / 3

def cone_generatrix(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Конус не существует"

    return math.sqrt(r * r + h * h)

def cone_base_area(r):
    r = make_positive(r)

    if r == 0:
        return "Конус не существует"

    return math.pi * r * r

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

def cylinder_form_menu():
    return (
        "Выбери формулу цилиндра:\n"
        "1) S = 2*pi*r*(r+h)\n"
        "2) S бок = 2*pi*r*h\n"
        "3) V = pi*r^2*h\n"
        "4) S осн = pi*r^2\n"
        "5) V = pi*d^2*h/4\n"
        "6) S бок = pi*d*h"
    )

def cylinder_area_full(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Цилиндр не существует"

    return 2 * math.pi * r * (r + h)

def cylinder_area_side(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Цилиндр не существует"

    return 2 * math.pi * r * h

def cylinder_volume(r, h):
    r = make_positive(r)
    h = make_positive(h)

    if r == 0 or h == 0:
        return "Цилиндр не существует"

    return math.pi * r * r * h

def cylinder_base_area(r):
    r = make_positive(r)

    if r == 0:
        return "Цилиндр не существует"

    return math.pi * r * r

def cylinder_volume_d(d, h):
    d = make_positive(d)
    h = make_positive(h)

    if d == 0 or h == 0:
        return "Цилиндр не существует"

    return math.pi * d * d * h / 4

def cylinder_area_side_d(d, h):
    d = make_positive(d)
    h = make_positive(h)

    if d == 0 or h == 0:
        return "Цилиндр не существует"

    return math.pi * d * h

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

def rhombus_form_menu():
    return (
        "Выбери формулу ромба:\n"
        "1) P = 4*a\n"
        "2) S = a*h\n"
        "3) S = d1*d2/2"
    )

def rhombus_perimetr(a):
    a = make_positive(a)

    if a == 0:
        return "Ромб не существует"

    return 4 * a

def rhombus_area_1(a, h):
    a = make_positive(a)
    h = make_positive(h)

    if a == 0 or h == 0:
        return "Ромб не существует"

    return a * h

def rhombus_area_2(d1, d2):
    d1 = make_positive(d1)
    d2 = make_positive(d2)

    if d1 == 0 or d2 == 0:
        return "Ромб не существует"

    return d1 * d2 / 2

def hexagon_form_menu():
    return (
        "Выбери формулу правильного шестиугольника:\n"
        "1) P = 6*a\n"
        "2) S = 3*sqrt(3)*a^2/2"
    )

def hexagon_perimetr(a):
    a = make_positive(a)

    if a == 0:
        return "Шестиугольник не существует"

    return 6 * a

def hexagon_area(a):
    a = make_positive(a)

    if a == 0:
        return "Шестиугольник не существует"

    return 3 * math.sqrt(3) * a * a / 2

def ring_area(R, r):
    R = make_positive(R)
    r = make_positive(r)

    if R == 0 or r == 0:
        return "Кольцо не существует"

    if r >= R:
        return "Кольцо не существует"

    return math.pi * (R * R - r * r)

def sector_arc_length(r, alpha):
    r = make_positive(r)

    if r == 0:
        return "Сектор не существует"

    if alpha <= 0 or alpha > 360:
        return "Сектор не существует"

    return 2 * math.pi * r * alpha / 360

def sector_area(r, alpha):
    r = make_positive(r)

    if r == 0:
        return "Сектор не существует"

    if alpha <= 0 or alpha > 360:
        return "Сектор не существует"

    return math.pi * r * r * alpha / 360