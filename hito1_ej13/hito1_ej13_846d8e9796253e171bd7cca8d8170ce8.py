numero = int(input("Ingrese un número entero: "))

divisor = 2
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
        numero = numero / divisor
    else:
        divisor += 1
