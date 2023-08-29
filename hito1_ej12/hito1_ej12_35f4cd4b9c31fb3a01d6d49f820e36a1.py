#Juego adivina mi número
from random import randint
from time import sleep

while True:
    num = int(input("introduce un numero: "))
    sec = randint(1,20)
    if num == sec:
        sleep(1)
        print("Adivinaste, mi número era ", sec)
        
    if num != sec:
        if num > sec:
            print("mi numero es menor")
        if num < sec:
            print("mi numero es mayor")
        print("Intento numero 2")
        sleep(1)
        num = int(input("introduce un numero: "))
        if num != sec:
            if num > sec:
                print("mi número es menor")
            if num < sec:
                print("mi número es mayor")
            print("intento numero 3")
            sleep(1)
            num = int(input("introduce un numero: "))
            if num != sec:
                if num > sec:
                    print("mi numero es menor")
                if num < sec:
                    print("mi numero es mayor")
                print("intento numero 4")
                sleep(1)
                num = int(input("introduce un numero: "))
                if num != sec:
                    if num > sec:
                        print("mi numero es menor")
                    if num < sec:
                        print("mi numero es mayor")
                    print("intento numero 5")
                    print("No adivinaste, mi nÚmero era ",sec)
                    sleep(1)
                    break