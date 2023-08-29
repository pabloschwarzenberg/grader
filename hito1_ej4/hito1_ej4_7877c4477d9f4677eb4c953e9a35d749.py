decimal = float(input("Ingrese N° decimal:"))

import math
cicles = 1
if(decimal%2==0):
    binario = '0'
else:
    binario = '1'
decimal = decimal//2

while cicles==1:
    if(decimal%2==0):
        numberBi = '0'
    else:
        numberBi = '1'
    decimal = decimal//2
    binario = binario+numberBi
    if(decimal==1):
        decimal = math.trunc(decimal)
        binario = binario+str(decimal)
        break
binarioReal = binario[::-1]
print("Resultado=",binarioReal)