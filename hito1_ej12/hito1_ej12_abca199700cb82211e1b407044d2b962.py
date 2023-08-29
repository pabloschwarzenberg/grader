#Juego adivina mi número
from random import randint
from time import sleep

while True:
    num = int(input("Ingrese un número"))
    secreto = randint(1,20)
    if num == secreto:
        sleep(1)
        print("Adivinaste, mi número era ", secreto)
        
    if num != secreto:
        if num > secreto:
            print("mi número es menor")
        if num < secreto:
            print("mi número es mayor")
        print("Intento 2")
        sleep(1)
        num = int(input("Ingrese un número"))
        if num != secreto:
            if num > secreto:
                print("mi número es menor")
            if num < secreto:
                print("mi número es mayor")
            print("Intento 3")
            sleep(1)
            num = int(input("Ingrese un numero"))
            if num != secreto:
                if num > secreto:
                    print("mi número es menor")
                if num < secreto:
                    print("mi número es mayor")
                print("Intento 4")
                sleep(1)
                num = int(input("Ingrese un numero"))
                if num != secreto:
                    if num > secreto:
                        print("mi número es menor")
                    if num < secreto:
                        print("mi número es mayor")
                    print("Intento 5")
                    print("No adivinaste, mi número era ",secreto)
                    sleep(1)
                    break