from config import load_config, CURRENT_VERSION, DEFAULT_CONFIG
from core import generate_password, random_number, urv, dsc, bmi, calculate_expression
from converters import (convert_temp, convert_dist, convert_speed, convert_volume, convert_mass, convert_area)
from geometry import *


def main():
    config = load_config()
    config_version = config["config"]["config_version"]

    while True:
        try:
            print()
            if CURRENT_VERSION != config_version:
                print(
                    "Несоответствие версий калькулятора и конфига:\n"
                    f"Версия программы: {CURRENT_VERSION}\n"
                    f"Версия конфига: {config_version}\n"
                    "Во избежание возможных проблем, пожалуйста удалите текущий конфиг\n"
                    "Он будет создан автоматически"
                )
                break   

            main_choice = input(
                "Что вы хотите: \n"
                "cal для калькулятора \n"
                "spv для вычислений \n"
                "ran для рандома \n"
                "info для информации \n"
                "config для просмотра конфигурации\n"
                "exit для выхода\n"
            ).strip().lower()

            if main_choice == "exit":
                print("Остановка")
                break

            elif main_choice == "info":
                print(
                    "Версия калькулятора на языке Python\n"
                    "Версия: 3.0 \n"
                    "Автор: ShipovskijKorp\n"
                    "devblog: 20\n"
                    "Tg: https://t.me/+_9Ho35Hbbe8zOTEy"
                )

            elif main_choice == "config":  
                print("\nТекущие настройки: ",DEFAULT_CONFIG,"\n")    

            elif main_choice == "cal":
                cal_choice = input(
                    "Выбери: \n"
                    "cal для калькулятора \n"
                    "urv для уравнений\n"
                    "dsc для калькулятора систем счислений\n"
                    "conv для конвертаций \n"
                    "bmi для индекса массы тела \n"
                ).strip().lower()

                if cal_choice == "cal":
                    expr = input("Введи выражение: ").strip()
                    print(calculate_expression(expr))

                elif cal_choice == "urv":
                    a = int(input("Введите коэффициент x^2: "))
                    b = int(input("Введите коэффициент x: "))
                    c = int(input("Введите свободный член: "))
                    print(urv(a, b, c))

                elif cal_choice == "dsc":
                    x = input("Введи значение: ").strip().upper()
                    input_base = int(input("Введи исходную систему счисления (2-36): "))
                    output_base = int(input("Введи конечную систему счисления (2-36): "))
                    print(dsc(x, input_base, output_base))

                elif cal_choice == "conv":
                    conv_mode = input(
                        "Конвертация:\n"
                        "dist - дистанция \n"
                        "speed - скорость \n"
                        "area - площадь\n"
                        "volume - объем\n"
                        "mass - масса\n"
                        "temp - температура\n"
                    ).strip().lower()

                    if conv_mode == "temp":
                        temp_mode = input("Выбери: ctf для C в F или ftc для F в C \n").strip().lower()
                        t = float(input("Введите температуру: "))
                        print(convert_temp(t, temp_mode))

                    elif conv_mode == "dist":
                        print("Доступные единицы: мм, см, дм, м, км")
                        distance = float(input("Введите значение: "))
                        input_dist_unit = input("Введите исходную величину: ").strip().lower()
                        output_dist_unit = input("Введите желаемую величину: ").strip().lower()
                        print(convert_dist(distance, input_dist_unit, output_dist_unit))

                    elif conv_mode == "speed":
                        print("Доступные единицы: м/с, км/ч")
                        speed = float(input("Введите значение: "))
                        input_speed_unit = input("Введите исходную величину: ").strip().lower()
                        output_speed_unit = input("Введите желаемую величину: ").strip().lower()
                        print(convert_speed(speed, input_speed_unit, output_speed_unit))

                    elif conv_mode == "volume":
                        print("Доступные единицы: мл, л, см3, м3")
                        volume = float(input("Введите значение: "))
                        input_volume_unit = input("Введите исходную величину: ").strip().lower()
                        output_volume_unit = input("Введите желаемую величину: ").strip().lower()
                        print(convert_volume(volume, input_volume_unit, output_volume_unit))

                    elif conv_mode == "mass":
                        print("Доступные единицы: мг, г, кг, ц, т, Кт, Мт")
                        mass = float(input("Введите значение: "))
                        input_mass_unit = input("Введите исходную величину: ").strip().lower()
                        output_mass_unit = input("Введите желаемую величину: ").strip().lower()
                        print(convert_mass(mass, input_mass_unit, output_mass_unit))

                    elif conv_mode == "area":
                        print("Доступные единицы: мм2, см2, м2, км2")
                        area = float(input("Введите значение: "))
                        input_area_unit = input("Введите исходную величину: ").strip().lower()
                        output_area_unit = input("Введите желаемую величину: ").strip().lower()
                        print(convert_area(area, input_area_unit, output_area_unit))

                    else:
                        print("Операция не найдена")

                elif cal_choice == "bmi":
                    h = float(input("Введите рост (см): "))
                    m = float(input("Введите вес (кг): "))
                    print(bmi(h, m))

                else:
                    print("Операция не найдена")

            elif main_choice == "ran":
                ran_choice = input(
                    "Выбери тип рандома: \n"
                    "num для числа \n"
                    "pas для пароля\n"
                ).strip().lower()

                if ran_choice == "num":
                    min_n = int(input("Введите нижнюю границу: "))
                    max_n = int(input("Введите верхнюю границу: "))
                    print("Результат:", random_number(min_n, max_n))

                elif ran_choice == "pas":
                    length = int(input("Введите длину пароля, максимум 1024: "))
                    print(generate_password(length, config))

                else:
                    print("Операция не найдена")

            elif main_choice == "spv":
                print("Доступные фигуры:\nquad, rect, paral, trian, trap, okr, oval\nqub, par, spher, con, cil")
                figure = input("Введите фигуру: ").strip().lower()

                if figure == "quad":
                    print(sp())
                    action = input("Введите действие: ").strip().lower()
                    a = float(input("Введите сторону a: "))
                    print("Результат:", square(a, action))

                elif figure == "rect":
                    print(sp())
                    action = input("Введите действие: ").strip().lower()
                    a = float(input("Введите сторону a: "))
                    b = float(input("Введите сторону b: "))
                    print("Результат:", rectangle(a, b, action))

                elif figure == "paral":
                    print(sp())
                    action = input("Введите действие: ").strip().lower()
                    a = float(input("Введите основание a: "))

                    if action == "p":
                        b = float(input("Введите сторону b: "))
                        print("Результат:", paral(a, b, action))

                    elif action == "s":
                        h = float(input("Введите высоту h: "))
                        print("Результат:", paral(a, h, action))

                    else:
                        print("Операция не найдена")

                elif figure == "trian":
                    print(sp())
                    action = input("Введите действие: ").strip().lower()

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

                        else:
                            print("Формула не найдена")

                    elif action == "p":
                        a = float(input("Введите сторону a: "))
                        b = float(input("Введите сторону b: "))
                        c = float(input("Введите сторону c: "))
                        print("Результат:", triangle_perimetr(a, b, c))

                    else:
                        print("Операция не найдена")

                elif figure == "trap":
                    print(sp())
                    action = input("Введите действие: ").strip().lower()

                    if action == "p":
                        a = float(input("Введите основание a: "))
                        b = float(input("Введите основание b: "))
                        c = float(input("Введите сторону c: "))
                        d = float(input("Введите сторону d: "))
                        print("Результат:", trapezoid(a, b, c, d, 0, action))

                    elif action == "s":
                        a = float(input("Введите основание a: "))
                        b = float(input("Введите основание b: "))
                        h = float(input("Введите высоту h: "))
                        print("Результат:", trapezoid(a, b, 0, 0, h, action))

                    else:
                        print("Операция не найдена")

                elif figure == "okr":
                    print(sl())
                    action = input("Введите действие: ").strip().lower()
                    r = float(input("Введите радиус r: "))
                    print("Результат:", circle(r, action))

                elif figure == "oval":
                    print(sl())
                    action = input("Введите действие: ").strip().lower()
                    a = float(input("Введите полуось a: "))
                    b = float(input("Введите полуось b: "))
                    print("Результат:", oval(a, b, action))

                elif figure == "qub":
                    print(sv())
                    action = input("Введите действие: ").strip().lower()
                    a = float(input("Введите сторону a: "))
                    print("Результат:", cube(a, action))

                elif figure == "par":
                    print(sv())
                    action = input("Введите действие: ").strip().lower()
                    a = float(input("Введите длину a: "))
                    b = float(input("Введите ширину b: "))
                    c = float(input("Введите высоту c: "))
                    print("Результат:", box(a, b, c, action))

                elif figure == "spher":
                    print("Выбери S или V")
                    action = input("Введите действие: ").strip().lower()
                    r = float(input("Введите радиус r: "))
                    print("Результат:", sphere(r, action))

                elif figure == "con":
                    print("Выбери S или V")
                    action = input("Введите действие: ").strip().lower()
                    r = float(input("Введите радиус r: "))
                    h = float(input("Введите высоту h: "))
                    print("Результат:", cone(r, h, action))

                elif figure == "cil":
                    print("Выбери S или V")
                    action = input("Введите действие: ").strip().lower()
                    r = float(input("Введите радиус r: "))
                    h = float(input("Введите высоту h: "))
                    print("Результат:", cylinder(r, h, action))

                else:
                    print("Операция не найдена")
                                
            else:
                print("Операция не найдена")

        except ValueError as err:
            print(f"Ошибка ввода, {err}")

        except ZeroDivisionError as err:
            print(f"Ошибка, одно из чисел в делении равно 0, {err}")


if __name__ == "__main__":
    main()