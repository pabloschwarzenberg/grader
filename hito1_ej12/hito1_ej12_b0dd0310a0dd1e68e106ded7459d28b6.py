import random
import sys
lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(lista_numeros)
a = lista_numeros[0]
jugador = input("Adivina el número: ")
contador = 1
while not int(jugador) == a:
    contador = contador + 1
    if int(jugador) > a:
        print("El número ingresado es mayor que el número secreto.")
        jugador = input("Adivina el número: ")
    if int(jugador) < a:
        print("El número ingresado es menor que el número secreto.")
        jugador = input("Adivina el número: ")
    if contador == 5:
        print("No adivinaste, mi número era", a)
        sys.exit()
if int(jugador) == a:
    print("Adivinaste, mi número era", a)
    sys.exit()
