#Juego adivina mi número
from random import randint
from time import sleep
while True:

    n = int(input("Ingrese un numero: "))
    n_secreto = randint(1,20)
    if n == n_secreto:
        sleep(1)
        print("Adivinasteeee, era ", n_secreto)
        
    if n != n_secreto:
        if n > n_secreto:
            print("EL numero es menor")
        if n < n_secreto:
            print("El numero es mayor")
        print("Intento 2")
        sleep(1)
        n = int(input("Ingrese un numero: "))
        if n != n_secreto:
            if n > n_secreto:
                print("El número es menor")
            if n < n_secreto:
                print("El número es mayor")
            print("Intento 3")
            sleep(1)
            n = int(input("Ingrese un numero: "))
            if n != n_secreto:
                if n > n_secreto:
                    print("El número es menor")
                if n < n_secreto:
                    print("El número es mayor")
                print("Intento 4")
                sleep(1)
                n = int(input("Ingrese un numero: "))
                if n != n_secreto:
                    if n > n_secreto:
                        print("El número es menor")
                    if n < n_secreto:
                        print("El número es mayor")
                    print("Intento 5")
                    print("No adivinastee! Lo siento, el número era ",n_secreto)
                    sleep(1)
                    break
 



   