#Juego adivina mi número
from random import randint
from time import sleep

while True:
    n = int(input("Ingrese un numero"))
    s = randint(1,20)
    if n == s:
        sleep(1)
        print("Adivinaste, mi número era ", s)
        
    if n != s:
        if n > s:
            print("mi número es menor")
        if n < s:
            print("mi número es mayor")
        print("Intento N°2")
        sleep(1)
        n = int(input("Ingrese un numero"))
        if n != s:
            if n > s:
                print("mi número es menor")
            if n < s:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            n = int(input("Ingrese un numero"))
            if n != s:
                if n > s:
                    print("mi número es menor")
                if n < s:
                    print("mi número es mayor")
                print("Intento N°4")
                sleep(1)
                n = int(input("Ingrese un numero"))
                if n != s:
                    if n > s:
                        print("mi número es menor")
                    if n < s:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",s)
                    sleep(1)
                    break      