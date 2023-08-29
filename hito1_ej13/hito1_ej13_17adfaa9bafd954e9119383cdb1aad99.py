#Factores Primos
numero = int(input("Ingrese un número: "))

divisor = 2
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
        numero //= divisor
    else:
        divisor += 1
