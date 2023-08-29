#Conversión de Decimal a Binario
import math
numero = int(input("Ingrese un numero decimal: "))
binario = ""

#PROCESAMIENTO Y SALIDA
if (numero > 0):
    while(numero > 0):
        if(numero%2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        numero = int(math.floor(numero/2))
else:
    if (numero == 0):
        binario = "0"
    else:
        binario = "No se puede convertir el numero, ingrese solo numero positivos estimado"
print("resultado="+binario)      