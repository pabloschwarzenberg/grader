#Juego adivina mi número #cambiar variables
import random
jugador=random.randint(1,20)
intentos=0
m=False
while intentos<5:
    q=int(input("ingrese un número:"))
    if q==jugador:
        print("Adivinaste, mi número era",jugador)
        break
    if q<jugador:
        print("El número ingresado es menor")
    if q>jugador:
        print("El número ingresado es mayor")
    intentos=intentos+1

if intentos==5:
    print("No adivinaste, mi número era",jugador) 
      