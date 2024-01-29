from math import sqrt, pi

figure = input("1-треугольник, 2-прямоугольник, 3-круг: ")
def triangle(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
def rectangle(a, b):
    return a * b
def circle(r):
    return pi * r ** 2
if figure == '1':
    AB = float(input("Первая сторона: "))
    BC = float(input("Вторая сторона: "))
    CA = float(input("Третья сторона: "))
    print("Площадь треугольника: %.2f" % triangle(AB, BC, CA))
elif figure == '2':
    l = float(input("Длина: "))
    w = float(input("Ширина: "))
    print("Площадь прямоугольника: %.2f" % rectangle(l, w))
elif figure == '3':
    rad = float(input("Радиус: "))
    print("Площадь круга: %.2f" % circle(rad))
else:
    print("Ошибка ввода")
