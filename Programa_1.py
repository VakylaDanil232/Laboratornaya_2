import math

print("Введите коэффициенты для уравнения: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

Discriminant = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % Discriminant)

if Discriminant > 0:
    x1 = (-b + math.sqrt(Discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(Discriminant)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif Discriminant == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
elif Discriminant < 0:
    x = -b /2*a
else:
    print("Корней нет")