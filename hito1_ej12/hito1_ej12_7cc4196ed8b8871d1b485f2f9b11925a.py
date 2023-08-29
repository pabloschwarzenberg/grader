from random import randint
from time import sleep

while True:
    numero = int(input("Introduce un numero"))
    secreto = randint(1,20)
    if numero == secreto:
        sleep(1)
        print("Adivinaste, mi número era ", secreto)
        break
    if numero != secreto:
        if numero > secreto:
            print("mi número es menor")
        if numero < secreto:
            print("mi número es mayor")
        print("Intento N°2")
        sleep(1)
        numero = int(input("Introduce un numero"))
        if numero != secreto:
            if numero > secreto:
                print("mi número es menor")
            if numero < secreto:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            numero = int(input("Ingresa un numero"))
            if numero != secreto:
                if numero > secreto:
                    print("mi número es menor")
                if numero < secreto:
                    print("mi número es mayor")
                print("Intento N°4")
                sleep(1)
                numero = int(input("Ingresa un numero"))
                if numero != secreto:
                    if numero > secreto:
                        print("mi número es menor")
                    if numero < secreto:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",secreto)
                    sleep(1)
                    break