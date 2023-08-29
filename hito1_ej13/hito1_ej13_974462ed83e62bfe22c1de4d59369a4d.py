FP = int(2)
numero =int(input("Ingrese el número"))

while (numero != 1):
    if (numero % FP == 0):
        print(str(FP) + " ")
        numero = numero / FP
    else:
        FP = FP + 1