#Conversión de Decimal a Binario
import math
n = float(input("Ingrese un numero decimal: "))
bin = ""
if n > 0:
    while n > 0:
        if (n % 2) == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin
        n = int(math.floor(n/2))
else:
    if n == 0:
        bin = "0"
    else:
        bin = "Ingrese un numero positivo"
print("Resultado ="+bin)