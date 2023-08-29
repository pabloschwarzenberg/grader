#Juego adivina mi número
from random import randint
from time import sleep

while True:
    num = int(input("Ingrese un numero: "))
    secreto = randint(1,20)
    if num == secreto:
        sleep(1)
        print("Adivinaste, mi número era: ", secreto)
        
    if num != secreto:
        if num > secreto:
            print("mi número es menor")
        if num < secreto:
            print("mi número es mayor")
        print("Intento N°2")
        sleep(1)
        num = int(input("Ingrese un numero: "))
        if num != secreto:
            if num > secreto:
                print("mi número es menor")
            if num < secreto:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            num = int(input("Ingrese un numero: "))
            if num != secreto:
                if num > secreto:
                    print("mi número es menor")
                if num < secreto:
                    print("mi número es mayor")
                print("Intento N°4")
                sleep(1)
                num = int(input("Ingrese un numero: "))
                if num != secreto:
                    if num > secreto:
                        print("mi número es menor")
                    if num < secreto:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No acertaste. mi número era: ",secreto)
                    sleep(1)
                    break