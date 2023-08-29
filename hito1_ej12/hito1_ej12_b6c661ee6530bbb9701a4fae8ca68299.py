#Juego adivina mi número
from random import *

numeroSecetro = randrange(1 , 20)
contadorIncorrectos = 0
salir = False
while (salir != True):
    numeroIngresado = int(input("Ingrese un numero: "))
    if contadorIncorrectos == 4:
        print("No adivinaste, mi número era {}".format(numeroSecetro))
        salir = True
    elif numeroSecetro > numeroIngresado:
        print("mi número es mayor")
        contadorIncorrectos += 1
    elif numeroSecetro < numeroIngresado:
        print("mi número es menor")
        contadorIncorrectos += 1
    elif numeroIngresado == numeroSecetro:
        print("Adivinaste, mi número era {}".format(numeroSecetro))
        salir = True