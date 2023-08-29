#Juego adivina mi número
import random

intentos = 0
numero = random.randint(0, 20)

while intentos < 5:
    adivina = int(input('Ingresa un número entre 0 y 20: '))
    intentos = intentos + 1

    if adivina < numero:
        print('¡Demasiado pequeño! , Piensa en un numero mayor!')

    if adivina > numero:
        print('¡Demasiado grande!, Piensa en un numero menor')


    if adivina == numero:
        break

if adivina == numero:

    print('Adivinaste, mi número era '+ str(numero))

if adivina != numero:

    print('No adivinaste, mi número era '+str(numero))
