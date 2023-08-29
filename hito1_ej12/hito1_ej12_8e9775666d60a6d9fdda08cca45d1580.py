#Juego adivina mi número
intentosRealizados=0

print("¡Hola! Hoy vamos a adivinar un numero")

import random

print("Bueno, estoy pensando en un número entre 1 y 20.")

numero = random.randint(1, 20)


while intentosRealizados < 6:
    estimacion = input("¿En que numero estoy pensando?")

    intentosRealizadost = intentosRealizados + 1
    
    if estimacion == numero:

        print(intentosRealizadost)

        print("Adivinaste, mi número era", numero)
        break

    if estimacion != numero:

        numero = str(numero)

        print("No adivinaste, mi número era" + numero)
        break