#Juego adivina mi número
import random
intentosRealizados = 0
numero = random.randint(1, 20)
while intentosRealizados < 5:
    estimacion = int(input('Adivina mi numero entre 1 y 20: '))
    intentosRealizados = intentosRealizados + 1
    if estimacion < numero:
        print('Tu estimación es muy baja.')
    if estimacion > numero:
        print('Tu estimación es muy alta.')
    if estimacion == numero:
        break
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Adivinaste, mi numero era',numero)
if estimacion != numero:
    numero = str(numero)
    print('No adivinaste, mi numero era',numero)