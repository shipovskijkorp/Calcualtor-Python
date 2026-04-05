from geometrylogic import *

def sp():
    return "Выбери P или S"

def sl():
    return "Выбери L или S"

def sv():
    return "Выбери S или V"

def spv_selector():
    print(
        "Доступные фигуры:\n"
        "quad, rect, paral, trian, trap, okr, oval\n"
        "qub, par, spher, con, cil\n"
        "romb, hex, ring, sect"
    )
    figure = input("Введите фигуру: ").strip().lower()

    if figure == "quad":
        action = input(
            "Выбери действие:\n"
            "p - периметр\n"
            "s - площадь\n"
            "d - диагональ\n"
            "sd - сторона через диагональ\n"
            "ds - площадь через диагональ\n"
        ).strip().lower()

        if action == "p" or action == "s":
            a = float(input("Введите сторону a: "))
            print("Результат:", square(a, action))

        elif action == "d":
            a = float(input("Введите сторону a: "))
            print("Результат:", square_diagonal(a))

        elif action == "sd":
            d = float(input("Введите диагональ d: "))
            print("Результат:", square_side_from_diagonal(d))

        elif action == "ds":
            d = float(input("Введите диагональ d: "))
            print("Результат:", square_area_from_diagonal(d))

        else:
            print("Операция не найдена")

    elif figure == "rect":
        action = input(
            "Выбери действие:\n"
            "p - периметр\n"
            "s - площадь\n"
            "d - диагональ\n"
        ).strip().lower()

        if action == "p" or action == "s":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            print("Результат:", rectangle(a, b, action))

        elif action == "d":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            print("Результат:", rectangle_diagonal(a, b))

        else:
            print("Операция не найдена")

    elif figure == "paral":
        action = input(
            "Выбери действие:\n"
            "p - периметр\n"
            "s - площадь через высоту\n"
            "sa - площадь через угол\n"
            "d1 - первая диагональ\n"
            "d2 - вторая диагональ\n"
        ).strip().lower()

        if action == "p":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            print("Результат:", paral(a, b, action))

        elif action == "s":
            a = float(input("Введите основание a: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", paral(a, h, action))

        elif action == "sa":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            alpha = float(input("Введите угол alpha в градусах: "))
            print("Результат:", paral_area_angle(a, b, alpha))

        elif action == "d1":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            alpha = float(input("Введите угол alpha в градусах: "))
            print("Результат:", paral_diagonal_1(a, b, alpha))

        elif action == "d2":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            alpha = float(input("Введите угол alpha в градусах: "))
            print("Результат:", paral_diagonal_2(a, b, alpha))

        else:
            print("Операция не найдена")

    elif figure == "trian":
        action = input(
            "Выбери действие:\n"
            "s - площадь\n"
            "p - периметр\n"
            "pp - полупериметр\n"
            "h - высота через площадь\n"
            "r - радиус вписанной окружности\n"
            "R - радиус описанной окружности\n"
            "c - гипотенуза прямоугольного треугольника\n"
            "kat - катет прямоугольного треугольника\n"
        ).strip().lower()

        if action == "s":
            print(trian_form_menu_s())
            choice = input("Введите номер формулы: ").strip()

            if choice == "1":
                a = float(input("Введите сторону a: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", triangle_area_1(a, h))

            elif choice == "2":
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                alpha = float(input("Введите угол alpha в градусах: "))
                print("Результат:", triangle_area_2(a, b, alpha))

            elif choice == "3":
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                c = float(input("Введите сторону c: "))
                print("Результат:", triangle_area_3(a, b, c))

            elif choice == "4":
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                c = float(input("Введите сторону c: "))
                r = float(input("Введите радиус описанной окружности R: "))
                print("Результат:", triangle_area_4(a, b, c, r))

            elif choice == "5":
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                c = float(input("Введите сторону c: "))
                r = float(input("Введите радиус вписанной окружности r: "))
                print("Результат:", triangle_area_5(a, b, c, r))

            elif choice == "6":
                c = float(input("Введите сторону c: "))
                h = float(input("Введите высоту h к стороне c: "))
                print("Результат:", triangle_area_6(c, h))

            elif choice == "7":
                a = float(input("Введите первый катет a: "))
                b = float(input("Введите второй катет b: "))
                print("Результат:", triangle_area_7(a, b))

            else:
                print("Формула не найдена")

        elif action == "p":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))
            print("Результат:", triangle_perimetr(a, b, c))

        elif action == "pp":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))
            print("Результат:", triangle_half_perimetr(a, b, c))

        elif action == "h":
            s = float(input("Введите площадь S: "))
            a = float(input("Введите сторону a: "))
            print("Результат:", triangle_height_from_area(s, a))

        elif action == "r":
            s = float(input("Введите площадь S: "))
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))
            print("Результат:", triangle_inradius(s, a, b, c))

        elif action == "R":
            s = float(input("Введите площадь S: "))
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))
            print("Результат:", triangle_circumradius(s, a, b, c))

        elif action == "c":
            a = float(input("Введите первый катет a: "))
            b = float(input("Введите второй катет b: "))
            print("Результат:", right_triangle_hypotenuse(a, b))

        elif action == "kat":
            c = float(input("Введите гипотенузу c: "))
            b = float(input("Введите известный катет b: "))
            print("Результат:", right_triangle_leg(c, b))

        else:
            print("Операция не найдена")

    elif figure == "trap":
        action = input(
            "Выбери действие:\n"
            "p - периметр\n"
            "s - площадь\n"
            "m - средняя линия\n"
            "h - высота через площадь\n"
            "c - боковая сторона равнобедренной трапеции\n"
        ).strip().lower()

        if action == "p":
            a = float(input("Введите основание a: "))
            b = float(input("Введите основание b: "))
            c = float(input("Введите сторону c: "))
            d = float(input("Введите сторону d: "))
            print("Результат:", trapezoid_perimetr(a, b, c, d))

        elif action == "s":
            print(trapezoid_form_menu_s())
            choice = input("Введите номер формулы: ").strip()

            if choice == "1":
                a = float(input("Введите основание a: "))
                b = float(input("Введите основание b: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", trapezoid_area_1(a, b, h))

            elif choice == "2":
                m = float(input("Введите среднюю линию m: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", trapezoid_area_2(m, h))

            else:
                print("Формула не найдена")

        elif action == "m":
            a = float(input("Введите основание a: "))
            b = float(input("Введите основание b: "))
            print("Результат:", trapezoid_middle_line(a, b))

        elif action == "h":
            s = float(input("Введите площадь S: "))
            a = float(input("Введите основание a: "))
            b = float(input("Введите основание b: "))
            print("Результат:", trapezoid_height_from_area(s, a, b))

        elif action == "c":
            a = float(input("Введите основание a: "))
            b = float(input("Введите основание b: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", trapezoid_equal_side(a, b, h))

        else:
            print("Операция не найдена")

    elif figure == "okr":
        action = input(
            "Выбери действие:\n"
            "l - длина окружности\n"
            "s - площадь круга\n"
            "rfd - радиус через диаметр\n"
            "dfr - диаметр через радиус\n"
            "rfl - радиус через длину\n"
        ).strip().lower()

        if action == "l":
            print(trian_form_menu_l())
            choice = input("Введите номер формулы: ").strip()

            if choice == "1":
                r = float(input("Введите радиус r: "))
                print("Результат:", circle_length_1(r))

            elif choice == "2":
                d = float(input("Введите диаметр d: "))
                print("Результат:", circle_length_2(d))

            else:
                print("Формула не найдена")

        elif action == "s":
            print(circle_area_menu())
            choice = input("Введите номер формулы: ").strip()

            if choice == "1":
                r = float(input("Введите радиус r: "))
                print("Результат:", circle_area_1(r))

            elif choice == "2":
                d = float(input("Введите диаметр d: "))
                print("Результат:", circle_area_2(d))

            elif choice == "3":
                l = float(input("Введите длину окружности L: "))
                print("Результат:", circle_area_3(l))

            else:
                print("Формула не найдена")

        elif action == "rfd":
            d = float(input("Введите диаметр d: "))
            print("Результат:", circle_radius_from_diameter(d))

        elif action == "dfr":
            r = float(input("Введите радиус r: "))
            print("Результат:", circle_diameter_from_radius(r))

        elif action == "rfl":
            l = float(input("Введите длину окружности L: "))
            print("Результат:", circle_radius_from_length(l))

        else:
            print("Операция не найдена")

    elif figure == "oval":
        action = input(
            "Выбери действие:\n"
            "s - площадь\n"
            "l1 - длина по простой формуле\n"
            "l2 - длина по более точной формуле\n"
        ).strip().lower()

        a = float(input("Введите полуось a: "))
        b = float(input("Введите полуось b: "))

        if action == "s":
            print("Результат:", oval(a, b, "s"))
        elif action == "l1":
            print("Результат:", oval(a, b, "l"))
        elif action == "l2":
            print("Результат:", oval_length_2(a, b))
        else:
            print("Операция не найдена")

    elif figure == "qub":
        action = input(
            "Выбери действие:\n"
            "s - полная площадь\n"
            "p - сумма ребер\n"
            "v - объем\n"
            "d1 - диагональ грани\n"
            "d2 - диагональ куба\n"
            "sb - боковая площадь\n"
        ).strip().lower()

        a = float(input("Введите сторону a: "))

        if action == "s" or action == "p" or action == "v":
            print("Результат:", cube(a, action))
        elif action == "d1":
            print("Результат:", cube_face_diagonal(a))
        elif action == "d2":
            print("Результат:", cube_diagonal(a))
        elif action == "sb":
            print("Результат:", cube_side_area(a))
        else:
            print("Операция не найдена")

    elif figure == "par":
        action = input(
            "Выбери действие:\n"
            "s - полная площадь\n"
            "p - сумма ребер\n"
            "v - объем\n"
            "d - диагональ\n"
            "b - площадь основания\n"
        ).strip().lower()

        if action == "b":
            a = float(input("Введите длину a: "))
            b = float(input("Введите ширину b: "))
            print("Результат:", box_base_area(a, b))

        elif action == "d":
            a = float(input("Введите длину a: "))
            b = float(input("Введите ширину b: "))
            c = float(input("Введите высоту c: "))
            print("Результат:", box_diagonal(a, b, c))

        elif action == "s" or action == "p" or action == "v":
            a = float(input("Введите длину a: "))
            b = float(input("Введите ширину b: "))
            c = float(input("Введите высоту c: "))
            print("Результат:", box(a, b, c, action))

        else:
            print("Операция не найдена")

    elif figure == "spher":
        action = input(
            "Выбери действие:\n"
            "s - площадь\n"
            "v - объем\n"
            "sd - площадь через диаметр\n"
            "rfd - радиус через диаметр\n"
            "dfr - диаметр через радиус\n"
        ).strip().lower()

        if action == "s":
            r = float(input("Введите радиус r: "))
            print("Результат:", sphere(r, "s"))

        elif action == "v":
            print(sphere_form_menu())
            choice = input("Введите номер формулы: ").strip()

            if choice == "2":
                r = float(input("Введите радиус r: "))
                print("Результат:", sphere(r, "v"))

            elif choice == "3":
                d = float(input("Введите диаметр d: "))
                print("Результат:", sphere_volume_d(d))

            else:
                print("Формула не найдена")

        elif action == "sd":
            d = float(input("Введите диаметр d: "))
            print("Результат:", sphere_area_d(d))

        elif action == "rfd":
            d = float(input("Введите диаметр d: "))
            print("Результат:", sphere_radius_from_diameter(d))

        elif action == "dfr":
            r = float(input("Введите радиус r: "))
            print("Результат:", sphere_diameter_from_radius(r))

        else:
            print("Операция не найдена")

    elif figure == "con":
        action = input(
            "Выбери действие:\n"
            "s - площадь\n"
            "v - объем\n"
            "l - образующая\n"
            "b - площадь основания\n"
        ).strip().lower()

        if action == "s":
            print(cone_form_menu())
            choice = input("Введите номер формулы: ").strip()

            if choice == "1":
                r = float(input("Введите радиус r: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", cone_area_full(r, h))

            elif choice == "2":
                r = float(input("Введите радиус r: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", cone_area_side(r, h))

            else:
                print("Формула не найдена")

        elif action == "v":
            r = float(input("Введите радиус r: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", cone_volume(r, h))

        elif action == "l":
            r = float(input("Введите радиус r: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", cone_generatrix(r, h))

        elif action == "b":
            r = float(input("Введите радиус r: "))
            print("Результат:", cone_base_area(r))

        else:
            print("Операция не найдена")

    elif figure == "cil":
        action = input(
            "Выбери действие:\n"
            "s - площадь\n"
            "v - объем\n"
            "b - площадь основания\n"
            "vd - объем через диаметр\n"
            "sd - боковая площадь через диаметр\n"
        ).strip().lower()

        if action == "s":
            print(cylinder_form_menu())
            choice = input("Введите номер формулы: ").strip()

            if choice == "1":
                r = float(input("Введите радиус r: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", cylinder_area_full(r, h))

            elif choice == "2":
                r = float(input("Введите радиус r: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", cylinder_area_side(r, h))

            else:
                print("Формула не найдена")

        elif action == "v":
            r = float(input("Введите радиус r: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", cylinder_volume(r, h))

        elif action == "b":
            r = float(input("Введите радиус r: "))
            print("Результат:", cylinder_base_area(r))

        elif action == "vd":
            d = float(input("Введите диаметр d: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", cylinder_volume_d(d, h))

        elif action == "sd":
            d = float(input("Введите диаметр d: "))
            h = float(input("Введите высоту h: "))
            print("Результат:", cylinder_area_side_d(d, h))

        else:
            print("Операция не найдена")

    elif figure == "romb":
        action = input(
            "Выбери действие:\n"
            "p - периметр\n"
            "s - площадь\n"
        ).strip().lower()

        if action == "p":
            a = float(input("Введите сторону a: "))
            print("Результат:", rhombus_perimetr(a))

        elif action == "s":
            print(rhombus_form_menu())
            choice = input("Введите номер формулы: ").strip()

            if choice == "2":
                a = float(input("Введите сторону a: "))
                h = float(input("Введите высоту h: "))
                print("Результат:", rhombus_area_1(a, h))

            elif choice == "3":
                d1 = float(input("Введите диагональ d1: "))
                d2 = float(input("Введите диагональ d2: "))
                print("Результат:", rhombus_area_2(d1, d2))

            else:
                print("Формула не найдена")

        else:
            print("Операция не найдена")

    elif figure == "hex":
        action = input(
            "Выбери действие:\n"
            "p - периметр\n"
            "s - площадь\n"
        ).strip().lower()

        a = float(input("Введите сторону a: "))

        if action == "p":
            print("Результат:", hexagon_perimetr(a))
        elif action == "s":
            print("Результат:", hexagon_area(a))
        else:
            print("Операция не найдена")

    elif figure == "ring":
        R = float(input("Введите внешний радиус R: "))
        r = float(input("Введите внутренний радиус r: "))
        print("Результат:", ring_area(R, r))

    elif figure == "sect":
        action = input(
            "Выбери действие:\n"
            "l - длина дуги\n"
            "s - площадь сектора\n"
        ).strip().lower()

        r = float(input("Введите радиус r: "))
        alpha = float(input("Введите угол alpha в градусах: "))

        if action == "l":
            print("Результат:", sector_arc_length(r, alpha))
        elif action == "s":
            print("Результат:", sector_area(r, alpha))
        else:
            print("Операция не найдена")

    else:
        print("Операция не найдена")