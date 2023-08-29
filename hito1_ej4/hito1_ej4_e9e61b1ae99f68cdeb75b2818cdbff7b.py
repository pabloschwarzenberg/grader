import math
numeros = float(input("Ingrese numero decimal:"))
binario = ""
if (numeros > 0):
    while (numeros > 0):
        if (numeros%2 == 0):
            binario = "0" + binario
        else:
            binario= "1" + binario
        numeros = int(math.floor(numeros/2))
else:
    if (numeros == 0):
        binario = "0"
    else:
        binario = "No se puede convertir"
print("resultado=", binario)

