import math


numero = float(input("ingrese numero decimal: "))
binario=""

if (numero>0):
    while(numero>0):
        if (numero%2==0):
            binario = "0" + binario
        else:
            binario = "1" + binario

        numero = int(math.floor(numero/2))

else:
    if (numero == 0):
        binario = "0"

    else:
        "nose puede convertir a binario"

print("resultado = " + binario)

        