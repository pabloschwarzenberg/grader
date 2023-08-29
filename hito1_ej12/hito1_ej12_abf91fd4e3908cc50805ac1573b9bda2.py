#Juego adivina mi número
import random

numero=random.randint(1,20)
h=5
n=0
while 0 <= h:

    print("Adivina mi numero entre el 1 y el 20")
    n=int(input("Adivina cual es: "))

    if n == numero:

        print("Adivinaste, mi numero era",numero)
        break

    if n > numero:

        if h==1:

            print("Mi numero es menor, te queda un intento")

        if h == 0:
            print("No adivinaste, mi numero era",numero)

        if h>1:
            print("Mi numero es menor, te quedan",h,"intentos")
        h-=1

    if n < numero:

        if h == 1:
            print("Mi numero es mayor, te queda un intento")

        if h == 0:
            print("No adivinaste, mi numero era",numero)

        if h>1:
            print("Mi numero es mayor, te quedan",h,"intentos")
        h-=1
      