#Juego adivina mi número
import random
intentosRealizados = 0

numero = random.randint(1, 20)
print('estoy pensando en un número entre 1 y 20.')
while intentosRealizados < 5:
    print('Intenta adivinar.')
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1
    if estimación < numero:
        print('mi numero es mayor')
    if estimación > numero:
        print('mi numero es menor')
    if estimación == numero:
        break
if estimación == numero:
    intentosRealizados = str(intentosRealizados)
    print('Adivinaste, mi número era ',numero)
if estimación != numero:
    numero = str(numero)
    print('no adivinaste, mi numero era ' + numero)
     