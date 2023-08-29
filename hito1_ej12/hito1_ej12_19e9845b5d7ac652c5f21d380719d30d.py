#Juego adivina mi número
from random import randint 
from time import sleep 
while True:
    numero=int(input("Ingrese un numero:"))
    secreto=randint(1,20)
    if numero==secreto:
        sleep(1)
        print("Adivinaste,mi numeroera",secreto)

    if numero !=secreto:
        if numero>secreto:
            print("mi numeroes menor ")
            if numero<secreto:
                print("mi numero es mayor ")
                print("Intento numero2 ")
                sleep(1)
                numero=int(input("Ingrese un numero:"))
                if numero!=secreto:
                    if numero>secreto:
                        print("moi numero es menor ")
                        if numero<secreto:
                            print("mi numero es mayor" )
                            print("intento numero 3 ")
                            sleep(1)
                            numero= int(input("Ingrese un numero : "))
                            if numero !=secreto: 
                                if numero>secreto:
                                    print("mi numeroe es menor ")
                                    if numero < secreto:
                                        print("mi numero es mayor ")
                                        print("intento numero 4")
                                        sleep(1)
                                        numeor=int(input("ingrese un  numero :"))}
                                        if numero!=secreto:
                                            if numero!=secreto:
                                                if numero>secreto: 
                                                    print("mi numero es menor")
                                                    if numero<secreto:
                                                        print("mi numero es mayor ")
                                                        print("Intento numero 5 ")
                                                        print("no adivinaste ,mi numero era ",secreto)
                                                        sleep(1)
                                                        break 