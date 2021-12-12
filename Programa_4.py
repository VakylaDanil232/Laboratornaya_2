from math import cos, factorial, radians
x = radians(float(input("Введите значение угла: ")))
n = int(input("Введите число: "))
cosinus = sum(
    pow(-1, i) * pow(x, 2 * i) / factorial(2 * i) for i in range(n))
print("cos  %s:" % cosinus)
# Функция pow(-1,i) означает -1^i
#Функция sum() начинает суммирование элементов последовательности