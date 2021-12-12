import math

print("Введите стороны треугольника:")
a = int(input("Первая сторона: "))
if a == 0 or a < 0:
    print("Сторона не может быть отрицательной или равна нулю: ")
    while a == 0 or a < 0:
        a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))
if b == 0 or b < 0:
    print("Сторона не может быть отрицательной или равна нулю: ")
    while b == 0 or b < 0:
        b = int(input("Вторая сторона: "))
storona3 = int(input("Третья сторона: "))
if storona3 == 0 or storona3 < 0:
    print("Сторона не может быть отрицательной или равна нулю: ")
    while storona3 == 0 or storona3 < 0:
        storona3 = int(input("Вторая сторона: "))

elif storona3 > (a+b) or (a+storona3) <  b or (storona3+b) < a:
    print("Неверные стороны треугольника")
if  a == b:
    print("True")
else:
    print("False")
