#Juego adivina mi número
import random

intentosRealizados = 0

print('¡Hola!')

número = random.randint(1, 20)
print('Estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 5:
    print('Intenta adivinar.') # Hay cuatro espacios delante de print.
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('Mi numero es mayor.') # Hay ocho espacios delante de print.

    if estimación > número:
        print('Mi numero es menor.')

    if estimación == número:
        break

if estimación == número:
    print("Adivinaste, mi número era ", número)

if estimación != número:
    número = str(número)
    print('No adivinaste, mi número era ' + número)