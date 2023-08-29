#Juego adivina mi número
      from random import randint
from time import sleep

while True:
    n = int(input("Ingrese Su Numero"))
    s = randint(1,20)
    if n == s:
        sleep(1)
        print("Has Adivinado, Mi Numero Era", s)
        
    if n != s:
        if n > s:
            print("Mi Numero Es Menor Que El Tuyo")
        if n < s:
            print("Mi Numero Es Mayor Que El Tuyo")
        print("Segundo Intento")
        sleep(1)
        n = int(input("Ingrese Su Numero"))
        if n != s:
            if n > s:
                print("Mi Numero Es Menor Que El Tuyo")
            if n < s:
                print("Mi Numero Es Mayor Que El Tuyo")
            print("Tercer Intento")
            sleep(1)
            n = int(input("Ingrese Su Numero"))
            if n != s:
                if n > s:
                    print("Mi Numero Es Menor Que El Tuyo")
                if n < s:
                    print("Mi Numero Es Mayor Que El Tuyo")
                print("Cuarto Intento")
                sleep(1)
                n = int(input("Ingrese Su Numero"))
                if n != s:
                    if n > s:
                        print("Mi Numero Es Menor Que El Tuyo")
                    if n < s:
                        print("Mi Numero Es Mayor Que El Tuyo")
                    print("Quinto Intento")
                    print("No Has Adivinado Mi Numero, Este Era",s)
                    sleep(1)
                    break