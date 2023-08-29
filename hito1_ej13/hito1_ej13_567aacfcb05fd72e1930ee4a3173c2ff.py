#Factores Primos

Numero = int(input("ingrese numero: "))
Factor = 2
while (Numero > 1):
    if (Numero % Factor == 0):
        print(Factor)
        Numero //= Factor
    else:
        Factor += 1