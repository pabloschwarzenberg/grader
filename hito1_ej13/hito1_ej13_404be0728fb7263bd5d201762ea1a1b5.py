#Factores Primos
numero = int(input("Ingrese el numero: "))
divisor = int(2)
while (numero!=1):
    if (numero % divisor == 0):
        print(str(divisor) + "")
        numero = numero / divisor
    else:
        divisor= divisor + 1     