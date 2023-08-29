#Juego adivina mi número
import random

intentos=5
numero_aleatorio=random.randint(1,20)
while intentos>0:
    n=int(input("ingrese un numero del 1 al 20: "))
    if n==numero_aleatorio:
        print("Adivinaste, mi número era: ",numero_aleatorio)
        break
    elif n>numero_aleatorio:
        print("mi numero es menor")
        intentos=intentos-1
    elif n<numero_aleatorio:
        print("mi numero es mayor")
        intentos=intentos-1
else:
    print("No adivinaste, mi número era:",numero_aleatorio)
