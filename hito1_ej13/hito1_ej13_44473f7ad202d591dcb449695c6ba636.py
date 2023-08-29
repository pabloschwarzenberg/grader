#Factores Primos
factprimo = int(2)
nent = int(input("Ingresa un N° entero: "))
while (nent != 1):
    if (nent % factprimo == 0):
        print(str(factprimo) + "")
        nent = nent // factprimo
    else:
        factprimo = factprimo + 1