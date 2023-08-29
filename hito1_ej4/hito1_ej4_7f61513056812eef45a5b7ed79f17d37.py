#Conversión de Decimal a Binario
import math
x=int(input("Ingrese numero que quiere convertir a binario: "))
y=bin(x)
print("resultado="+y[2::])