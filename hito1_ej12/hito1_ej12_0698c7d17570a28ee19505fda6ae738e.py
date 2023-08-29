#Juego adivina mi número
from random import randint
from time import sleep
while True:
    número = int(input("Ingrese un número"))
    secreto = randint(1,20)
    if número == secreto:
        sleep(1)
        print("Adivinaste, mi número era ", secreto)    
    if número != secreto:
        if número > secreto:
            print("mi número es menor")
        if número < secreto:
            print("mi número es mayor")
        print("Intento N°2")
        sleep(1)
        número = int(input("Ingrese un numero"))
        if número != secreto:
            if número > secreto:
                print("mi número es menor")
            if número < secreto:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            número = int(input("Ingrese un numero"))
            if número != secreto:
                if número > secreto:
                    print("mi número es menor")
                if número < secreto:
                    print("mi número es mayor")
                print("Intento N°4")
                sleep(1)
                número = int(input("Ingrese un numero"))
                if número != secreto:
                    if número > secreto:
                        print("mi número es menor")
                    if número < secreto:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",secreto)
                    sleep(1)
                    break      