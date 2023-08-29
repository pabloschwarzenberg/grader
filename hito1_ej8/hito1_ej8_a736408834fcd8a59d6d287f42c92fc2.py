#Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles.
from os import system
system ("cls")
numero = input("Ingresa un numero de hasta 4 digitos: ")

if len(numero) > 4:
    print("Numero invalido")
else:
    numero = numero.zfill(4)

    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M+"
    if centenas > 0:
        descomposicion += str(centenas) + "C+"
    if decenas > 0:
        descomposicion += str(decenas) + "D+"
    if decenas ==0:
        descomposicion += "0D+"
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    print(descomposicion)