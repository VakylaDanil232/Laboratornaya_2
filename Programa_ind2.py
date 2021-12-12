for i in range(10, 100):

   summ = 0

   i = str(i)

   for k in range(len(i)):

       summ += int(i[k])

   if summ % 5 == 0:

       print(i, end=' ')
