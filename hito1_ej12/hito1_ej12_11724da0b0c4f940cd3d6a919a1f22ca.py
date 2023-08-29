#Juego adivina mi número
from random import randint
from time import sleep
while True:
    x = int(input("Ingresa un numero"))
    MiNumero = randint(1,20)
    if x == MiNumero:
        sleep(1)
        print("Adivinaste, mi número era", MiNumero)

    if x != MiNumero:
        if x > MiNumero:
            print("Mi número es menor al tuyo")
        if x < MiNumero:
            print("Mi número es mayor al tuyo")
        print("Intento N°2")
        sleep(1)
        x = int(input("Ingresa un numero"))
        if x != MiNumero:
            if x > MiNumero:
                print("mi número es menor al tuyo")
            if x < MiNumero:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            numero = int(input("Ingresa un numero"))
            if x != MiNumero:
                if x > MiNumero:
                    print("mi número es menor al tuyo")
                if x < MiNumero:
                    print("mi número es mayor al tuyo")
                print("Intento N°4")
                sleep(1)
                numero = int(input("Ingresa un numero"))
                if x != MiNumero:
                    if x > MiNumero:
                        print("mi número es menor al tuyo")
                    if x < MiNumero:
                        print("mi número es mayor al tuyo")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",MiNumero)
                    sleep(1)
                    break  