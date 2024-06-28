import math
while True:
    a = int(input("Введите коэффициент а: \n"))
    b = int(input("Введите коэффициент b: \n"))
    c = int(input("Введите коэффициент с: \n"))
    print(f"Ваше уравнение: {a}x^2 + {b}x + {c}")
    D = b**2 - (4*a*c)
    if D < 0:
        print("Решение: Нет корней")
    elif D == 0:
        print(f"Решение: x = {-b/(2*a)}")
    else:
        print(f"Решение: x1 ={(-b + math.sqrt(D))/(2*a)}, x2 = {(-b - math.sqrt(D))/(2*a)} ")
