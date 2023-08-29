#Factores Primos
x = int(2)
Numero = int(input("Ingrese un valor: "))

while (Numero != 1):
    if (Numero % x == 0):
        print(str(x) + " ")
        Numero = Numero / x
    else:
        x = x + 1      