import math


numerox = int(input("Ingrese numero decimal:"))

binarios = ""

if (numerox > 0):

    while (numerox > 0):

        if (numerox%2 == 0):

            binarios = "0" + binarios

        else:

            binarios= "1" + binarios

        numerox = int(math.floor(numerox/2))

else:

    if (numerox == 0):

        binarios = "0"

    else:

        binarios = "No se puede convertir"

print("resultado=",binarios)



