#Juego adivina mi número
from random import randint
from time import sleep

while True:
    a = int(input("Ingrese un numero: "))
    s = randint(1,20)
    if a == s:
        sleep(1)
        print("Adivinaste, mi número era ", s)

    if a != s:
        if a > s:
            print("Mi número es menor")
        if a < s:
            print("Mi número es mayor")
        print("Intento N°2")
        sleep(1)
        a = int(input("Ingrese un numero"))
        if a != s:
            if a > s:
                print("Mi número es menor")
            if a < s:
                print("Mi número es mayor")
            print("Intento N°3")
            sleep(1)
            a = int(input("Ingrese un numero"))
            if a != s:
                if a > s:
                    print("Mi número es menor")
                if a < s:
                    print("Mi número es mayor")
                print("Intento N°4")
                sleep(1)
                a = int(input("Ingrese un numero: "))
                if a != s:
                    if a > s:
                        print("Mi número es menor")
                    if a < s:
                        print("Mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ", s)
                    sleep(1)
                    break      