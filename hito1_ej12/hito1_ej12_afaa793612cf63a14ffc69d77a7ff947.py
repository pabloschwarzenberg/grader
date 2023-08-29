#Juego adivina mi número
from random import randint
numero = randint(1,20)
adivinar =eval(input("ingresa el numero:"))
if adivinar < numero:
    print("mi numero es mayor")
if adivinar > numero:
    print("mi numero es mayor")
if adivinar == numero:
    print("adivinaste mi numero, mi numero era:", numero)      