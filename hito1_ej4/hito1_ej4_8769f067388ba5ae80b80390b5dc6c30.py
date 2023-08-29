#Conversión de Decimal a Binario
import math
Decimal = int(input("Ingrese un número: "))
Binario = ""
if(Decimal>=0):
    while(Decimal>0):
        if(Decimal%2==0):
            Binario = "0" + Binario
        else:
            Binario = "1" + Binario
        Decimal = int(math.floor(Decimal/2))
else:
    if(Decimal==0):
        Binario = "0"
print("resultado=",Binario)