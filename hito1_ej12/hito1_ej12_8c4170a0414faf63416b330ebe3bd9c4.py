#Juego adivina mi número
from random import randint
from time import sleep

while True:
    
    v = int(input("Inserte un valor"))
    x = randint(1,20)
    
    if v == x:
        sleep(1)
        
        print("Acertaste, mi valor es: ", x)
        
    if v != x:
        if v > x:
            print("mi número es menor")
        if v < x:
            print("mi número es mayor")
        print("Intento N°2")
        sleep(1)
        v = str(input("Ingrese un numero"))
        if v != x:
            if v > x:
                print("mi número es menor")
            if v < x:
                print("mi número es mayor")
            print("Intento N°3")
            sleep(1)
            v = int(input("Ingrese un numero"))
            if v != x:
                if v > x:
                    print("mi número es menor")
                if v < x:
                    print("mi número es mayor")
                print("Intento N°4")
                sleep(1)
                v = int(input("Ingrese un numero"))
                if v != x:
                    if v > x:
                        print("mi número es menor")
                    if v < x:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",x)
                    sleep(1)
                    break