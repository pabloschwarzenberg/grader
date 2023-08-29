#Factores Primos
FP = int(2)
numero = int(input("ingrese valor: "))

while (numero != 1):
    if (numero % FP == 0):
        print(str(FP) + " ")
        numero = numero / FP
    else:
        FP = FP + 1      