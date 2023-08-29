#Factores Primos
num = int(input("Ingrese cualquier numero: "))

c = 2

while c <= num:
    if num%c == 0:
         print(c)
         num = num / c
    else: 
       c = c + 1
     