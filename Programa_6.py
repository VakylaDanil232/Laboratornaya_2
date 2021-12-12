age = int(input("Введите возраст: "))
if age < 1 or age > 100:
        print("Возраст не может быть больше 100 или меньше 1")
        while age < 1 or age > 100:
            age = int(input("Введите  возраст: "))
if (age % 10 == 1) and (age != 11) and (age != 111):

        print("Вам", age, "год")
elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
  print("Вам", age, "года")
else:
 print("Вам", age, "лет")
