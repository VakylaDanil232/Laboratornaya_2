print("Введите число: ")

f1 = 1
f2 = 1
n = int(input())
print("Ряд Фибоначчи: ")
print(f1)
print(f2)
while n>2:
     f1, f2 = f2, f1 + f2 # f1 присваивается f2,а к f2 присваивается f1+ f2
     print(f2)
     n = n -1
