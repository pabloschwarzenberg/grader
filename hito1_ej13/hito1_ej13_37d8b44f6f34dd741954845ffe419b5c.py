#Factores Primos
num = int(input("Ingrese el número ->"))

if num > 1:
    for primos in range(2,num):
        resto = num % primos
        if resto == 0:
            print(primos)     