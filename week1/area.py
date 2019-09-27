import math

tip = str(input("Введите название фигуры = "))
if tip == "треугольник":
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    c = float(input("Введите сторону c = "))
    p = (a + b + c) / 2
    s = math.sqrt((p * (p - a) * (p - b) * (p - c)))
    print("%.1f" % s)
elif tip == "прямоугольник":
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    s = a * b
    print("%.1f" % s)
elif tip == "круг":
    r = float(input("Введите радиус r = "))
    s = math.pi * (r ** 2)
    print("%.1f" % s)
