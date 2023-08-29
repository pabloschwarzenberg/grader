#Conversión de Decimal a Binario
import math

x = int(input("Ingrese un número decimal: "))
binario = ""

while x > 0:
    if x%2 == 0:
        binario = "0" + binario
    else:
        binario = "1" + binario
    x = int(math.floor(x/2))
    
print("Resultado=", binario)
     