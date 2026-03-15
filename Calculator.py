import math
from math import sqrt
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:

    try:
        choice = input("Что вы хотите: \ncal для калькулятора \nspv для вычислений \nran для рандома \ndop для дополнительных функций \ninfo для информации \nexit для выхода\n").strip().lower()

        if choice == 'cal':
            choice = input("Выбери: \ncal для калькулятора \nurv для уравнений\n").strip().lower()
            if choice == 'cal':
                x = float(input("Введи первое число: "))
                y = float(input("Введи второе число: "))

                choice = input("Выбери операцию: +, -, *, /, sr (сравнение) : ").strip().lower()

                if choice == '+':
                    print("Результат: ", x + y)

                elif choice == '-':
                    print("Результат: ", x - y)

                elif choice == '*':
                    print("Результат: ", x * y)

                elif choice == '/':
                    if y == 0:
                        print("На 0 делить  нельзя (РКН запретил)")

                    else:
                        print("Результат: ", x / y)

                elif choice == 'sr':
                    if x > y:
                        print(x, ">", y)

                    elif x == y:
                        print(x, "=", y)

                    else:
                        print(x, "<", y)

                else:
                    print("Ненайдена операция")

            elif choice == 'urv':
                a = int(input("Введите коффициэнт х квадрата: "))
                b = int(input("Введите коффициэнт обычного х: "))
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
                        x1 = ((-b) + sqrt(d)) / (2*a)
                        x1 = round(x1, 2)
                        x2 = ((-b) - sqrt(d)) / (2*a)
                        x2 = round(x2, 2)
                        print("x1 =", x1, "x2 =", x2)

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
            print("Версия калькулятора на языке Python\nВерсия: 2.8.5 \nАвтор: ShipovskijKorp\ndevblog: 16\nTg: https://t.me/+_9Ho35Hbbe8zOTEy")

        elif choice == 'dop':
            choice = input("\nВыбери: \nconv для конвертаций \nimb для индекса массы тела \nstg для генерации историй \nrps для игры камень ножницы бумага \ndev для функций разработчика\n").strip().lower()
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
                names = [' Антон', ' Игорь', ' Максим', ' Иван', ' Кирил']
                action2 = [' шел', ' бежал', ' бродил']
                action = [' увидел', ' заметил']
                action3 = [' взял', ' подобрал']
                place = [' городу', ' лесу', ' полю']
                item = [' сотку', ' пяти десятку', ' пятисотку', ' тысчу']
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

            elif choice == 'dev':
                dev = input("2st для вывода 2 значных в столбик \n3st для вывода 3 значных в столбик \nkib для киберone \nEoO для сравнения кто старше\n").strip().lower()

                if dev == '2st':
                    zn2 = int(input("Введи 2 значное число: "))
                    if zn2 < 10 or zn2 > 99:
                        print("Это не 2 значное число")
                        continue
                    print("Результат: ")
                    a1 = zn2//10
                    print(a1)
                    a2 = zn2 % 10
                    print(a2)

                    dev1answer = input("Хотите сумму? (да/нет): ").strip().lower()

                    if dev1answer == 'да':
                        print("Результат: ")
                        print(a1+a2)

                    elif dev1answer == 'нет':
                        print()

                    else:
                        print("Ненайдена операция")

                elif dev == '3st':
                    zn3 = int(input("Введи 3 значное число: "))
                    if zn3 < 100 or zn3 > 999:
                        print("Это не 3 значное число")
                        continue
                    print("Результат: ")
                    a1 = zn3//100
                    print(a1)
                    a2 = zn3//10 % 10
                    print(a2)
                    a3 = zn3 % 10
                    print(a3)

                    dev1answer = input("Хотите сумму? (да/нет): ").strip().lower()

                    if dev1answer == 'да':
                        print("Результат: ")
                        print(a1+a2+a3)

                    elif dev1answer == 'нет':
                        print()

                    else:
                        print("Ненайдена операция")

                elif dev == 'kib':
                    kib5 = int(input("Введите количесво 5: "))
                    if kib5 < 0:
                        print("Отрицательное значение преобразовано в положительное")
                        kib5 = -kib5
                    kib10 = int(input("Введите количесво 10: "))
                    if kib10 < 0:
                        print("Отрицательное значение преобразовано в положительное")
                        kib10 = -kib10
                    kib20 = int(input("Введите количесво 20: "))
                    if kib20 < 0:
                        print("Отрицательное значение преобразовано в положительное")
                        kib20 = -kib20
                    kib50 = int(input("Введите количесво 50: "))
                    if kib50 < 0:
                        print("Отрицательное значение преобразовано в положительное")
                        kib50 = -kib50
                    kibe = kib5*5 + kib10*10 + kib20*20 + kib50*50
                    print("Результат:", kibe)

                elif dev == 'EoO':
                    name1 = input("Введите первое имя: ")
                    age1 = int(input("Введите первый возраст: "))
                    name2 = input("Введите второе имя: ")
                    age2 = int(input("Введите второй возраст: "))
                    name3 = input("Введите третье имя: ")
                    age3 = int(input("Введите третий возраст: "))

                    if age1 > age2 and age1 > age3:
                        print(name1, "старше всех")

                    elif age2 > age1 and age2 > age3:
                        print(name2, "старше всех")

                    elif age3 > age2 and age3 > age1:
                        print(name3, "старше всех")

                    elif age1 == age2 and age1 > age3:
                        print(name1, "и", name2, "старше чем", name3)

                    elif age2 == age3 and age2 > age1:
                        print(name2, "и", name3, "старше чем", name1)

                    elif age1 == age3 and age1 > age2:
                        print(name1, "и", name3, "старше чем", name2)

                    elif age1 == age2 and age1 == age3:
                        print(name1, name2, "и", name3, "одного возраста")

                else:
                    print("Ненайдена операция")

            elif choice == 'rps':
                print("Данная функция на техническом обслуживании")
                #enemylist = ['Камень', 'Ножницы', 'Бумага']
                #enemy = random.choice(enemylist)
                #player = input("Введи свой жест: ")

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
                spv = input("Выбери: \nP - периметр \nS - для площади \nV - для обьема \n").strip().lower()
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
                spv = input("Выбери: \nP - периметр \nS - для площади \nV - для обьема \n").strip().lower()
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
                spv = input("Выбери: \nS - для площади \nV - для обьема \n").strip().lower()
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
                spv = input("Выбери: \nS - для площади \nV - для обьема \n").strip().lower()
                if spv == 's':
                    x = float(input("Введи радиус: "))
                    y = float(input("Введи высоту: "))
                    if x < 0:
                        print("Радиус не может быть отрицательным, отрицательное значение преобразовано в положительное")
                        x = -x
                    if y < 0:
                        print("Сторона не может быть отрицательна, отрицательное значение преобразовано в положительное")
                        y = -y 
                    l = sqrt(x*x + y*y)
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
                spv = input("Выбери: \nS - для площади \nV - для обьема \n").strip().lower()
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
        print("Ошибка, одно из чисел в делении равно 0")    