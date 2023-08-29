#Juego adivina mi número
contador=1
import sys
import random

computador=random.randint(1,20)

while contador<=5 :
    jugador=input("Inserte número:")

    jugador=int(jugador)

    
    if jugador==computador:
        print("Adivinaste, mi número era",computador)

        break
    

    elif jugador>=computador:
        print("El número es menor.")
        contador=(contador+1)

    elif jugador<=computador:
        print("El número es mayor.")
        contador=(contador+1)

    

print("No adivinaste, mi número era",computador)




      