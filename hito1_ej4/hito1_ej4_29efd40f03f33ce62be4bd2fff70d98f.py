#Conversión de Decimal a Binario
import math

num=int(input("Ingrese un número entero: "))

binario=''

if(num>0):
    while(num>0):
        if(num%2==0):
            binario='0'+binario
        else:
            binario='1'+binario

        num=int(math.floor(num/2))

else:
    if(numero==0):
        binario='0'
    else:
        binario="No se puede convertir número"

print("Resultado=",binario)

