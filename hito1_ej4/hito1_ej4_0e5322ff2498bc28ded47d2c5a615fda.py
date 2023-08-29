import math
decimal= int(input("Ingrese su numero decimal a convertir en binario:"))
binario=""
divisor=2
if (decimal > 0):
    while (decimal > 0):
        if (decimal % 2 == 0):
            binario=str(binario)
            binario="0" + binario
        else:
            binario=str(binario)
            binario= "1" + binario
        decimal= int(math.floor(decimal/2))
else:
    if (decimal== 0):
        binario="0"
    else:
        binario= "no se puede convertir en binario"
print("resultado:"+ binario)