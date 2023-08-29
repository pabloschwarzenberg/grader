#Factores Primos
print("Descomposicion de numeros primos")
X = int(2)
Numero = int(input("ingrese valor: "))

while (Numero != 1):
    if (Numero % X == 0):
        print(str(X) + " ")
        Numero = Numero / X
    else:
        X = X + 1      