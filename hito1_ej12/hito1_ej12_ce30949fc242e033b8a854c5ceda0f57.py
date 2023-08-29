#Juego adivina mi número
import random
intentosRealizados = 0

numero = random.randint(1, 20)
print('estoy pensando en un número entre 1 y 20.')
while intentosRealizados < 5:
    print('Intenta adivinar.') 
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimación es muy baja.') 

    if estimacion > numero:
        print('Tu estimación es muy alta.')

    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print(' adivinaste mi número era ' + intentosRealizados )

if estimacion != numero:
    numero = str(numero)
    print('no adivinaste mi numero era' + numero)