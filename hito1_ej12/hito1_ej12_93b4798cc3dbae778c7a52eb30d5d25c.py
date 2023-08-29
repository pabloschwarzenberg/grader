#Juego adivina mi número
import random

computador=random.randint(1,20)
contador=0
while contador<5:
    jugador=int(input("Numero:"))
    if jugador == computador:
        print("Tu ganas")
        break
    if jugador > computador:
        print("tu numero es mayor")
        contador+=1

    if jugador < computador:
        print("tu numero es menor")
        contador+=1
    if contador ==5:
        print("has perdido")
        