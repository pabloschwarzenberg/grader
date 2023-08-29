#Juego adivina mi número
import random
intentos = 5
número = random.randint(1, 20)
print('Bueno, estoy pensando en un número entre 1 y 20.')
while intentos > 0:
    print('Intenta adivinar.') # Hay cuatro espacios delante de print.
    estimación = int(input())
    #estimación = int(estimación)
    intentosRealizados = intentos - 1
    if estimación < número:
        print('Tu estimación es muy baja.') # Hay ocho espacios delante de print.
    if estimación > número:
        print('Tu estimación es muy alta.')
    if estimación == número:
        break
if estimación == número:
    intentos = str(intentos)
    print("Adivinaste, mi número era ", número)
if estimación != número:
    print("No adivinaste, mi número era ",número)