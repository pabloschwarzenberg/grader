#Juego adivina mi número
from random import *
print("Estoy pensando en un número entre 1 y 20: ")
a = randint(1,20)
intentos=5
while intentos >0:
    adivina = int(input("Adivina el número:"))
    intentos = intentos-1
    print("intentos restantes:",intentos)
    if adivina < a:
        print("mi número es menor")
    if adivina > a:
        print("mi número es mayor")
    if adivina == a:
        break
      