print("Введите количество слагаемых после Pi/4: ")
n = int(input())
n = n - 1
s = 1
l = 3
for i in range(n):
        if i % 2 == 0:
            s = s - 1 / l
        else:
            s = s + 1 / l
l += 2
s = s * 4
print(s)
