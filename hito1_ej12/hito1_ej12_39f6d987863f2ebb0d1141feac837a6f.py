#Juego adivina mi número
from random import randint

numero= randint(1,20)

intentos= 0
continuar= "si"
while continuar == "si" and intentos!=5:

    intento= int(input("ingresa un numero: "))
    if intento==numero:
        continuar= "no"
        print("Adivinaste, mi numero era",numero)
    elif intento>numero:
        print("mi numero es menor")
    elif intento<numero:
        print("mi numero es mayor")
    intentos= intentos + 1
if intentos==5 and continuar=="si":
    print("No adivinaste, mi numero era",numero)

    