#Factores Primos
x = int(2)
numero = int(input("ingrese un número"))
while (numero != 1):
    if (numero % x == 0):
        print(x)
        numero = numero / x
    else:
        x = x + 1
