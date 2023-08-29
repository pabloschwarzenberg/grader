#Conversión de Decimal a Binario
#math import como ensenado hoy, usar while 
import math

numero = int(input("Ingrese un numero positivo decimal:"))
binario = ""
if numero > 0:
    while numero > 0:
        if numero % 2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        numero = int(math.floor(numero / 2))
else:
    if (numero == 0):
        binario = "0"
    else:
        binario = "Volver a ingresar un numero positivo "
print("resultado= ", binario)
