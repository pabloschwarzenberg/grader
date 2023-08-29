#Juego adivina mi número
from random import randint
from time import sleep

while True:
    Numero = int(input("Ingrese un numero"))
    Secreto = randint(1,20)

    if Numero == Secreto:
        sleep(1)
        print("Adivinaste, mi número era ", secreto)
        
    if Numero != Secreto:

        if Numero > Secreto:
            print("mi número es menor")

        if Numero < Secreto:
            print("mi número es mayor")
        print("Segundo intento")
        sleep(1)
        Numero = int(input("Ingrese un numero"))

        if Numero != Secreto:

            if Numero > Secreto:
                print("mi número es menor")

            if Numero < Secreto:
                print("mi número es mayor")
            print("Tercer intento")
            sleep(1)
            Numero = int(input("Ingrese un numero"))

            if Numero != Secreto:

                if Numero > Secreto:
                    print("mi número es menor")

                if Numero < Secreto:
                    print("mi número es mayor")
                print("Cuarto intento")
                sleep(1)
                Numero = int(input("Ingrese un número"))

                if Numero != Secreto:

                    if Numero > Secreto:
                        print("mi número es menor")

                    if Numero < Secreto:
                        print("mi número es mayor")
                    print("Quinto intento")
                    print("No adivinaste, mi número era ",Secreto)
                    sleep(1)
                    break      