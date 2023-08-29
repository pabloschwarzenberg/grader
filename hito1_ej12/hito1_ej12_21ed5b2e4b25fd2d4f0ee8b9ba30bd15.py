#Juego adivina mi número
import random

from random import randint

adivinar = random.randint(1,20)

intentos = 0

while intentos < 6:

 if intentos == 5:
    print("No adivinaste mi numero era " + str(adivinar))
    break

 numero = int(input("ingresar un numero: "))

 if numero < adivinar:
    print("mi número es mayor")
    intentos = intentos + 1

 if numero > adivinar:
    print("mi número es menor")
    intentos = intentos + 1

 if numero == adivinar:
    print("Adivinaste, mi número era " + str(adivinar))
    break