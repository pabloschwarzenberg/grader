#Juego adivina mi número
from random import randint
from time import sleep

while True:
    nro = int(input("Ingrese un numero para iniciar:"))
    nrosecreto = randint(1, 20)
    if nro == nrosecreto:
        sleep(1)
        print("Descubriste mi número secreto! era: ", nrosecreto)

    if nro != nrosecreto:
        if nro > nrosecreto:
            print("mi número es menor a eso!")
        if nro < nrosecreto:
            print("mi número es mayor a eso!")
        print("2do Intento!")
        sleep(1)
        nro = int(input("Ingrese un numero (denuevo jaja):"))
        if nro != nrosecreto:
            if nro > nrosecreto:
                print("mi número es menor")
            if nro < nrosecreto:
                print("mi número es mayor a eso!")
            print("3er Intento")
            sleep(1)
            nro = int(input("Ingrese un numero: (otra vez?)"))
            if nro != nrosecreto:
                if nro > nrosecreto:
                    print("mi número es menor")
                if nro < nrosecreto:
                    print("mi número es mayor a eso!")
                print("4to Intento!")
                sleep(1)
                nro = int(input("Ingrese un numero: (aún no puedes?)"))
                if nro != nrosecreto:
                    if nro > nrosecreto:
                        print("mi número es menor")
                    if nro < nrosecreto:
                        print("mi número es mayor")
                    print("5to (Y ULTIMO) Intento")
                    print("Yo gano! no adivinaste, mi número era: ", nrosecreto)
                    sleep(1)
                    break