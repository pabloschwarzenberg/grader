#Juego adivina mi número
from random import randint
from time import sleep

while True:
    numero = int(input("Ingrese un numero:"))
    secreto = randint(1, 20)
    if numero == secreto:
        print("Adivinaste, mi numero era", secreto)
        sleep(1)
    if numero != secreto:
        if numero > secreto:
            print("mi numero es menor")
        if numero < secreto:
            print("mi numero es mayor")
        print("Intento N°2")
        sleep(1)
        numero = int(input("Ingrese un numero:"))
    if numero != secreto:
        if numero > secreto:
            print("mi numero es menor")
        if numero < secreto:
            print("mi numero es mayor")
        print("Intento N°3")
        sleep(1)
        numero = int(input("Ingrese un numero:"))
    if numero != secreto:
        if numero > secreto:
            print("mi numero es menor")
        if numero < secreto:
            print("mi numero es mayor")
        print("Intento N°4")
        sleep(1)
        numero = int(input("Ingrese un numero:"))
    if numero != secreto:
        if numero > secreto:
            print("mi numero es menor")
        if numero < secreto:
            print("mi numero es mayor")
        print("Intento N°5")
        print("No adivinaste mi numero, era : ", secreto)
        sleep(1)
        break
if numero == secreto:
    print("Adivinaste, mi numero era", secreto)
     