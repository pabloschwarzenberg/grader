#Juego adivina mi número
from random import randint
from time import sleep

while True:
    numero = int(input("Ingrese un numero: "))
    secreto = randint(1,20)
    if numero == secreto:
        print("ADIVINASTE, mi numero era: ", secreto)
    if numero != secreto:
        if numero > secreto:
            print("Mi numero es menor: ")
        if numero < secreto:
            print("Mi numero es mayor: ")
    if numero == secreto:
                print("ADIVINASTE, mi numero era: ", secreto)
                break
    print("Intento 2")
    numero = int(input("Ingrese un numero: "))
    if numero != secreto:
        if numero > secreto:
            print("Mi numero es menor: ")
        if numero < secreto:
            print("Mi numero es mayor: ")
    if numero == secreto:
        print("ADIVINASTE, mi numero era: ", secreto)
        break
    print("Intento 3")
    numero = int(input("Ingrese un numero: "))
    if numero != secreto:
        if numero > secreto:
            print("Mi numero es menor: ")
        if numero < secreto:
                    print("Mi numero es mayor: ")
    if numero == secreto:
        print("ADIVINASTE, mi numero era: ", secreto)
        break
    print("Intento 4")
    numero = int(input("Ingrese un numero: "))
    if numero != secreto:
        if numero > secreto:
            print("Mi numero es menor: ")
        if numero < secreto:
            print("Mi numero es mayor: ")
    if numero == secreto:
        print("ADIVINASTE, mi número era: ", secreto)
        break
    print("Intento N°5")
    numero = int(input("Ingrese un numero: "))
    if numero != secreto:
        if numero > secreto:
            print("Mi numero es menor: ")
        if numero < secreto:
            print("Mi numero es mayor: ")
    if numero == secreto:
        print("ADIVINASTE, mi numero era: ", secreto)
        break

    print("NO ADIVINASTE, mi numero era: ",secreto)
    break      