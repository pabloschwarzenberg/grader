 # Este es el juego de adivinar el número.

import random

intentosRealizados = 0

numero = random.randint(1, 20)

while intentosRealizados < 5:
    print("Intenta adivinar.") 
    estimación = input()
    estimación = int(estimación)
    intentosRealizados = intentosRealizados + 1
    if estimación < numero:

        print("El numero es mayor") 


    if estimación > numero:
        print("El numero es menor")
        
        if estimación == numero:
            break

if estimación == numero:
    print("Adivinaste mi numero era: ", numero )


if estimación != numero:
    numero = str(numero)
    print("No adivinaste, mi numero era:", numero)
