#Juego adivina mi número
from random import randint
from time import sleep

while True:
    numerito = int(input("Ingrese un numero: "))
    secre_tito = randint(1,20)
    if numerito == secre_tito:
        sleep(1)
        print("Adivinaste<3, el número era: ", secre_tito)
        
    if numerito != secre_tito:
        if numerito > secre_tito:
            print("Mi número es menor juj")
        if numerito < secre_tito:
            print("Mi número es mayor juj")
        print("Intento N°2")
        sleep(1)
        numerito = int(input("Ingrese un numero: "))
        if numerito != secre_tito:
            if numerito > secre_tito:
                print("Mi número es menor juj")
            if numerito < secre_tito:
                print("Mi número es mayor juj")
            print("Intento N°3")
            sleep(1)
            numerito= int(input("Ingrese un numero: "))
            if numerito != secre_tito:
                if numerito > secre_tito:
                    print("Mi número es menor juj")
                if numerito < secre_tito:
                    print("Mi número es mayor juj")
                print("Intento N°4")
                sleep(1)
                numerito = int(input("Ingrese un numero: "))
                if numerito != secre_tito:
                    if numerito > secre_tito:
                        print("Mi número es menor juj")
                    if numerito < secre_tito:
                        print("Mi número es mayor juj")
                    print("Intento N°5")
                    print("No adivinaste:(, el número era: ",secre_tito)
                    sleep(1)
                    break     