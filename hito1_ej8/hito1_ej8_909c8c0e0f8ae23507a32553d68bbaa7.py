#Descomponer un número
num=str(input())
if len(num) == 4:
   mil=(num[0:1])
   cen=(num[1:2])
   dec=(num[2:3])
   uni=(num[3:4])
   print ((mil + "M +"), (cen + "C +"), (dec + "D +"), (uni + "U"))
if len(num) == 3:
    cen=(num[0:1])
    dec=(num[1:2])
    uni=(num[2:3])
    print ((cen + "C +"), (dec + "D +"), (uni + "U"))
if len(num) == 2:
    dec=(num[0:1])
    uni=(num[1:2])
    print ((dec + "D +"), (uni + "U"))
if len(num) == 1:
    print (uni + "U")