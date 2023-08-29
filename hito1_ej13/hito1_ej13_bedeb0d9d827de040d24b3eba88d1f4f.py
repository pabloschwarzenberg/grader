#Factores Primos
num = int(input("ingresa un numero: "))

factor = 2
while factor <= num:
    if num%factor == 0:
        print(factor)
        num = num / factor
    else:
        factor= factor + 1 


     