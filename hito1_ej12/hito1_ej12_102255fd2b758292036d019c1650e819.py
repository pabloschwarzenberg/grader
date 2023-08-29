#Juego adivina mi número
from random import *
print("Estoy pensando en un número entre 1 y 20: ")
a = randint(1,20)
intentos=0
while intentos < 5:
    adivina = int(input("Adivina el número:"))
    intentos = intentos+1

    if adivina < a:
        print("mi número es menor")
    if adivina > a:
        print("mi número es mayor")
    if adivina == a:
        break



if adivina == a:
    print("Adivinaste, mi número era " + str(a))
if adivina != a:
    print("No adivinaste, mi número era " + str(a))      