#Juego adivina mi número
from random import randint
numero = randint(1,20)
intento = 1
while intento <= 5:
    numUser= int(input("ingresa numero: "))
    if numero < numUser:
        print("mi número es menor")
        intento += 1
    if numero > numUser:
        print("mi número es mayor")
        intento += 1
    if numero==numUser:
        print("Adivinaste, mi número era ",numero)
        intento += 7
if intento==5:
    print("No adivinaste, mi número era ",numero)