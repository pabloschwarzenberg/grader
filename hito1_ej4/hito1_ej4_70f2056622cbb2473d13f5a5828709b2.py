#Conversión de Decimal a Binario
from os import system
system ("cls")

decimal = int(input("Ingresa un número decimal: "))
binario = bin(decimal)[2:]
print("resultado=", binario)