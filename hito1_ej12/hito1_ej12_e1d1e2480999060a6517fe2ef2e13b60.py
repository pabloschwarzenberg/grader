import random
intentosRealizados = 0
numero = random.randint(1, 20)
print('\nEstoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    estimacion = 5
    intentosRealizados = intentosRealizados + 1
    if estimacion < numero:
        print('\nmi número es mayor')
    if estimacion > numero:
        print('\nmi número es menor')
    if estimacion == numero:
        break
if estimacion == numero:
    numero = str(numero)
    estimacion = str(estimacion)
    print('Adivinaste, mi número era ' + numero)

if estimacion != numero:
    numero = str(numero)
    estimacion = str(estimacion)
    print('No adivinaste, mi número era ' + numero)