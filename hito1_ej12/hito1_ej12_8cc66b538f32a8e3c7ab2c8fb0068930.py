#Juego adivina mi número

import random
numero=random.randint(1,20)
i=0

while True:
    jugador=int(input("Ingrese un número entre 1 y 20: "))
    i+=1
    if(jugador < numero):
        print("El número a adivinar es mayor")
    elif(jugador==numero):
        print("Adivinaste, mi número era", numero)
        break
    else:
        print("El número a adivinar es menor")
    if i==5:
        print("No adivinaste, mi número era", numero)
        break      