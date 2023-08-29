#Juego adivina mi número
import random
import sys

numero = random.randint(1,20)
intentos = 5
adivinar = int(input("Adivina mi numero, tienes solo 5 intentos: "))

while intentos > 1:
    if adivinar > numero:
        print("Mi numero es menor")
        intentos = intentos - 1
        adivinar = int(input("Adivina mi numero, tienes solo 5 intentos: "))

    elif adivinar < numero:
        print("Mi numero es mayor")
        intentos = intentos - 1
        adivinar = int(input("Adivina mi numero, tienes solo 5 intentos: "))

    elif adivinar == numero:
        print("Adivinaste, mi número era {}".format(numero))
        sys.exit()

if intentos == 1:
    print("No adivinaste, mi número era {}".format(numero))      