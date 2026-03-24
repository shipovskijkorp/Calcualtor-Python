import math
import secrets
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

while True:

    try:
        choice = input("Что вы хотите: \ncal для калькулятора \nspv для вычислений \nran для рандома \ndop для дополнительных функций \ninfo для информации \nexit для выхода\n").strip().lower()

        if choice == 'cal':
            choice = input("Выбери: \ncal для калькулятора \nurv для уравнений\ndsc для калькулятора систем счислений\n").strip().lower()
            if choice == 'cal':

                expr = input("Введи выражение: ")
                expr = expr.replace("^", "**")
                result = eval(expr)
                print("Результат:", result)

            elif choice == 'urv':
                a = int(input("Введите коэффициент х квадрата: "))
                b = int(input("Введите коэффициент обычного х: "))
                c = int(input("Введите последнее число: "))

                if a == 0:
                    if b == 0:
                        if c == 0:
                            print("Бесконечно много решений")
                        else:
                            print("Нет решений")
                    else:
                        x = -c / b
                        x = round(x, 2)
                        print("x =", x)
                else:
                    d = b**2 - 4*a*c

                    if d < 0:
                        print("Нет корней")
                        
                    elif d == 0:
                        x = (-b) / (2 * a)
                        x = round(x, 2)
                        print("x =", x)
                    else:
                        x1 = ((-b) + math.sqrt(d)) / (2*a)
                        x1 = round(x1, 2)
                        x2 = ((-b) - math.sqrt(d)) / (2*a)
                        x2 = round(x2, 2)
                        print("x1 =", x1, "x2 =", x2)

            elif choice == 'dsc':
                x = input("Введи значение: ").upper()
                input_base = int(input("Введи исходную систему счисления (2-36): "))
                output_base = int(input("Введи конечную систему счисления (2-36): "))

                digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                result = ""

                if input_base < 2 or input_base > 36 or output_base < 2 or output_base > 36:
                    print("Такой системы счисления не существует")
                else:
                    a = int(x, input_base)

                    if a == 0:
                        result = "0"
                    else:
                        while a > 0:
                            result = digits[a % output_base] + result
                            a = a // output_base

                    print("Ответ: ", result)

            else:
                print("Ненайдена операция") 

        elif choice == 'ran':

            choice = input("Выбери тип рандома: \nnum для числа (0-10) \npas для пароля: ").strip().lower()

            if choice == 'num':
                print("Результат:", random.randint(0, 10))

            elif choice == 'pas':
                password_length = int(input("Введите длину пароля, максимум 1024: "))
                if password_length < 0:
                    password_length *= -1
                    print("Отрицательная длина не поддерживается, введенная преобразована в положительную")

                    if password_length > 1024:
                        print("Длина пароля ограничена 1024 символами, длина пароля обрезана до 1024")
                        password_length = 1024    
                        generated_password = generate_password(password_length)
                        print("Твой пароль: ", generated_password)
                    else:    
                        generated_password = generate_password(password_length)
                        print("Твой пароль: ", generated_password)

                elif password_length == 0:
                    print("Пароля с длинной 0 не существует")
                elif password_length > 1024:
                    print("Длина пароля ограничена 1024 символами, длина пароля обрезана до 1024")
                    password_length = 1024    
                    generated_password = generate_password(password_length)
                    print("Твой пароль: ", generated_password)
                else:    
                    generated_password = generate_password(password_length)
                    print("Твой пароль: ", generated_password)

            else:
                print("Ненайдена операция")

        elif choice == 'info':
            print("Версия калькулятора на языке Python\nВерсия: 2.9.1 legacy \nАвтор: ShipovskijKorp\ndevblog: 19\nTg: https://t.me/+_9Ho35Hbbe8zOTEy")

        elif choice == 'dop':
            choice = input("\nВыбери: \nconv для конвертаций \nimb для индекса массы тела \nstg для генерации историй \nrps для игры камень ножницы бумага \nkib для киберone\n").strip().lower()
            if choice == 'imb':
                H = float(input("Введите рост (см): "))
                if H == 0:
                    print("Рост не может быть равен 0!")
                    continue
                elif H < 0:
                    H = -H
                    print("Рост не может быть отрицательным, отрицательное значение конвертировано в положительное")  
                elif H < 140:
                    print("Хоббиты общий сбор!!!")      
                M = float(input("Введите вес (кг): "))
                if M == 0:
                    print("Вес не может быть равен 0!")
                    continue
                elif M < 0:
                    M = -M
                    print("Вес не может быть отрицательным, отрицательное значение конвертировано в положительное")
      
                H2 = H/100
                index = M/(H2*H2)
                print("Результат:", round(index, 1))
            elif choice == 'conv':
                conv = input("dist - конвертация дистанции \ntemp для конвертации температуры\n").strip().lower()
                if conv == 'dist':
                    print("1) мм в см \n2) мм в м \n3) мм в км\n4) см в мм \n5) см в м \n6) см в км \n7) м в мм \n8) м в см \n9) м в км \n10) км в мм \n11) км в см \n12) км в м ")
                    conv = int(input("Выберете операцию: "))
                    dist = float(input("Введите число: "))

                    if conv == 1:
                        print("Результат: ", dist/10, " см")

                    elif conv == 2:
                        print("Результат: ", dist/1000, " м")

                    elif conv == 3:
                        print("Результат: ", dist/1000000, " км")

                    elif conv == 4:
                        print("Результат: ", dist*10, " мм")

                    elif conv == 5:
                        print("Результат: ", dist/100, " м")

                    elif conv == 6:
                        print("Результат: ", dist/100000, " км")

                    elif conv == 7:
                        print("Результат: ", dist*1000, " мм")

                    elif conv == 8:
                        print("Результат: ", dist*100, " см")

                    elif conv == 9:
                        print("Результат: ", dist/1000, " км")

                    elif conv == 10:
                        print("Результат: ", dist*1000000, " мм")

                    elif conv == 11:
                        print("Результат: ", dist*100000, " см")

                    elif conv == 12:
                        print("Результат: ", dist*1000, " м")

                    else:
                        print("Ненайдена операция")

                elif conv == 'temp':
                    tempt = input("Выбери: ctf для C в F или ftc для F в C \n").strip().lower()
                    if tempt == 'ctf':
                        t = float(input("Введите температуру: "))
                        print(t * 1.8 + 32, "F")
                    elif tempt == 'ftc':
                        t = float(input("Введите температуру: "))
                        print((t-32) * 5/9, "C")
                    else:
                        print("Ненайдена операция")

                else:
                    print("Ненайдена операция")

            elif choice == 'stg':
                time0 = ['Однажды', 'Вчера', 'Утром', 'Год назад', 'В первом классе', 'После того как посрал']
                names = [' Антон', ' Игорь', ' Максим', ' Иван', ' Кирилл']
                action2 = [' шел', ' бежал', ' бродил']
                action = [' увидел', ' заметил']
                action3 = [' взял', ' подобрал']
                place = [' городу', ' лесу', ' полю']
                item = [' сотку', ' пяти десятку', ' пятисотку', ' косарь']
                action4 = [' и ушел', ' и убежал']
                print(random.choice(time0)+random.choice(names)+random.choice(action2), " по", random.choice(place), " и", random.choice(action)+random.choice(item), ", он", random.choice(action3), "ее", random.choice(action4))
                item2 = [' кириeшки', ' хавчик', ' колу' ]
                action5 = ['купил']
                place2 = ['Пятерочке', 'Магните', 'ларьке']
                time2 = ['Потом']
                print(random.choice(time2), "он", random.choice(action5)+random.choice(item2), "в", random.choice(place2))
                time3 = ['Потом', 'Позже']
                action6 = [' украл', ' стырил']
                print(random.choice(time3)+random.choice(names)+random.choice(action6), " у него это")

            elif choice == 'kib':
                kib5 = int(input("Введите количество 5: "))
                if kib5 < 0:
                    print("Отрицательное значение преобразовано в положительное")
                    kib5 = -kib5
                kib10 = int(input("Введите количество 10: "))
                if kib10 < 0:
                    print("Отрицательное значение преобразовано в положительное")
                    kib10 = -kib10
                kib20 = int(input("Введите количество 20: "))
                if kib20 < 0:
                    print("Отрицательное значение преобразовано в положительное")
                    kib20 = -kib20
                kib50 = int(input("Введите количесво 50: "))
                if kib50 < 0:
                    print("Отрицательное значение преобразовано в положительное")
                    kib50 = -kib50
                kib100 = int(input("Введите количесво 100: "))  
                if kib100 < 0:
                    print("Отрицательное значение преобразовано в положительное")
                    kib100 = -kib100  
                kibe = kib5*5 + kib10*10 + kib20*20 + kib50*50 + kib100*100
                print("Результат:", kibe)

            elif choice == 'rps':
                enemylist = ['камень', 'ножницы', 'бумага']
                enemy = random.choice(enemylist)
                player = input("Введи свой жест: ").strip().lower()
                if player == enemy:
                    print("Ничья, противник тоже выбрал:", enemy)
                elif player == "бумага" and enemy == "камень":
                    print("Ты выиграл,", "противник выбрал:", enemy)
                elif player == "ножницы" and enemy == "камень":
                    print("Ты проиграл,", "противник выбрал:", enemy)      
                elif player == "ножницы" and enemy == "бумага":
                    print("Ты выиграл,", "противник выбрал:", enemy)
                elif player == "камень" and enemy == "бумага":
                    print("Ты проиграл,", "противник выбрал:", enemy)  
                elif player == "камень" and enemy == "ножницы":
                    print("Ты выиграл,", "противник выбрал:", enemy)
                elif player == "бумага" and enemy == "ножницы":
                    print("Ты проиграл,", "противник выбрал:", enemy)  
                else:
                    print("Ты ввел неправильный жест")            

            else:
                print("Ненайдена операция")

        elif choice == 'spv':
            fig = input("\nquad, rect, trian, trap, okr\nqub, par, spher, con, cil \nВведи название фигуры: ").strip().lower()
            if fig == 'quad':
                spv = input("Выбери: \nP - периметр \nS - для площади \n").strip().lower()
                if spv == 'p':
                    x = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", x*4, "см")

                elif spv == 's':
                    x = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", x*x, "см2")

                else:
                    print("Ненайдена операция")

            elif fig == 'rect':
                spv = input("Выбери: \nP - периметр \nS - для площади \n").strip().lower()
                if spv == 'p':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y    
                    print("Результат: ", x*2 + y*2, "см")

                elif spv == 's':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y  
                    print("Результат: ", x*y, "см2")

                else:
                    print("Ненайдена операция")

            elif fig == 'trian':
                spv = input("Выбери: \nP - периметр \nS - для площади \n").strip().lower()
                if spv == 'p':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    z = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    if z < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        z = -z     
                    print("Результат: ", x+y+z, "см")

                elif spv == 's':
                    x = float(input("Введи основание: "))
                    y = float(input("Введи высоту: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    print("Результат: ", (x*y)/2, "см2")

                else:
                    print("Ненайдена операция")

            elif fig == 'trap':
                spv = input("Выбери: \nP - периметр \nS - для площади \n").strip().lower()
                if spv == 'p':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    z = float(input("Введи сторону: "))
                    w = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    if z < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        z = -z 
                    if w < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        w = -w     
                    print("Результат: ", x+y+z+w, "см")

                elif spv == 's':
                    x = float(input("Введи основание: "))
                    y = float(input("Введи основание: "))
                    z = float(input("Введи высоту: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    if z < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        z = -z 
                    print("Результат: ", (x+y)/2*z, "см2")

                else:
                    print("Ненайдена операция")

            elif fig == 'okr':
                spv = input("Выбери: \nP - периметр \nS - для площади \n").strip().lower()
                if spv == 'p':
                    r = float(input("Введи радиус: "))
                    if r < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        r = -r
                    print("Результат: ", 2*r*math.pi, "см")

                elif spv == 's':
                    r = float(input("Введи радиус: "))
                    if r < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        r = -r
                    print("Результат: ", math.pi*r*r, "см2")

                else:
                    print("Ненайдена операция")

            elif fig == 'qub':
                spv = input("Выбери: \nP - периметр \nS - для площади \nV - для объема \n").strip().lower()
                if spv == 'p':
                    x = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", x*12, "см")

                elif spv == 's':
                    x = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", 6*x*x, "см2")

                elif spv == 'v':
                    x = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", x*x*x, "см3")

                else:
                    print("Ненайдена операция")

            elif fig == 'par':
                spv = input("Выбери: \nP - периметр \nS - для площади \nV - для объема \n").strip().lower()
                if spv == 'p':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    z = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    if z < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        z = -z     
                    print("Результат: ", x*4 + y*4 + z*4, "см")

                elif spv == 's':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    z = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    if z < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        z = -z 
                    print("Результат: ", (x*y + y*z + z*x)*2, "см2")

                elif spv == 'v':
                    x = float(input("Введи сторону: "))
                    y = float(input("Введи сторону: "))
                    z = float(input("Введи сторону: "))
                    if x < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    if z < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        z = -z 
                    print("Результат: ", x*z*y, "см3")

                else:
                    print("Ненайдена операция")

            elif fig == 'spher':
                spv = input("Выбери: \nS - для площади \nV - для объема \n").strip().lower()
                if spv == 's':
                    x = float(input("Введи радиус: "))
                    if x < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", 4*x*math.pi*x, "см2")

                elif spv == 'v':
                    x = float(input("Введи радиус: "))
                    if x < 0:
                        print("Радиус не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        x = -x
                    print("Результат: ", (4/3)*math.pi*x*x*x, "см3")

                elif spv == 'p':
                    print("НУ ты дурак совсем?")

                else:
                    print("Ненайдена операция")

            elif fig == 'con':
                spv = input("Выбери: \nS - для площади \nV - для объема \n").strip().lower()
                if spv == 's':
                    x = float(input("Введи радиус: "))
                    y = float(input("Введи высоту: "))
                    if x < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    l = math.sqrt(x*x + y*y)
                    print("Результат: ", math.pi*x*l + math.pi*x*x, "см2")

                elif spv == 'v':
                    x = float(input("Введи радиус: "))
                    y = float(input("Введи высоту: "))
                    if x < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    print("Результат: ", (1/3)*math.pi*x*x*y, "см3")

                elif spv == 'p':
                    print("НУ ты дурак совсем?")    

                else:
                    print("Ненайдена операция")

            elif fig == 'cil':
                spv = input("Выбери: \nS - для площади \nV - для объема \n").strip().lower()
                if spv == 's':
                    x = float(input("Введи радиус: "))
                    y = float(input("Введи высоту: "))
                    if x < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    print("Результат: ", 2*math.pi*x*y + 2*math.pi*x*x, "см2")

                elif spv == 'v':
                    x = float(input("Введи радиус: "))
                    y = float(input("Введи высоту: "))
                    if x < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    print("Результат: ", math.pi*x*x*y, "см3")

                else:
                    print("Ненайдена операция")
            else:
                print("Ненайдена фигура")
        elif choice == 'exit':
            print("Остановка")
            break        
        else:
            print("Ненайдена операция")

    except ValueError:
        print("Ошибка ввода")
    except ZeroDivisionError:
        print("Ошибка, одно из чисел в делении равно 0") #дополнительная проверка для неожиданных сценариев