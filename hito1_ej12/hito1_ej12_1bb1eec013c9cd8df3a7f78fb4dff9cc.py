#Juego adivina mi número
import random
intentosRealizados = 0

número = random.randint(1, 20)
print('Adivina un número entre 1 y 20, tienes 5 intentos: ')
while intentosRealizados <= 4:
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('mi numero es mayor')

    if estimación > número:
        print('mi numero es menor')

    if estimación == número:
        break

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('Adivinaste, mi numero era', + número)

if estimación != número:
    número = str(número)
    print('No adivinaste, mi número era ' + número)