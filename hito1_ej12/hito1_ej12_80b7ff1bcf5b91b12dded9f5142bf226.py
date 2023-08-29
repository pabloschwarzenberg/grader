#Juego adivina mi número
import random
numero=random.randint(1,20)
i=-1

while i<6:
    i=i+1
    jugador=int(input("Adivina mi numero (entre 1 y 20): "))
    if jugador==numero:
        print("Adivinaste, mi número era", str(numero))
        break
    elif i==5:
        print("No adivinaste, mi número era ", str(numero))
        break
    elif jugador<numero:
        print("es mayor")
    elif jugador>numero:
        print("es menor")
    