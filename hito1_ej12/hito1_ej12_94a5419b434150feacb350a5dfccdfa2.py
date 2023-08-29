#Juego adivina mi número
import random as rd 
from time import sleep

while True:
    n = int(input("Ingrese un numero"))
    sh = rd.randint(1,20)
    if n == sh:
        sleep(1)
        print("Adivinaste, mi número era ", sh)

    if n != sh:
        if n > sh:
            print("mi número es menor")
        if n < sh:
            print("mi número es mayor")
        print("Intento N°2")
        sleep(1)
        n = int(input("Ingrese un numero"))
        if n!= sh:
            if n > sh:
                print("mi número es menor")
            if n < sh:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            n = int(input("Ingrese un numero"))
            if n != sh:
                if n > sh:
                    print("mi número es menor")
                if n < sh:
                    print("mi número es mayor")
                print("Intento N°4")
                sleep(1)
                n = int(input("Ingrese un numero"))
                if n != sh:
                    if n > sh:
                        print("mi número es menor")
                    if n < sh:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",sh)
                    sleep(1)
                    break
      