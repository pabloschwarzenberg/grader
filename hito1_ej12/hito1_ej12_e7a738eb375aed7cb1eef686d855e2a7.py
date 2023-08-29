#Juego adivina mi número
import random

intentos = 0


numero = random.randint(1, 20)
print('Bueno, piensa un número entre 1 y 20.')

while intentos < 5:
    print('Adivínalo Tienes 5 intentos')
    adivina = input()
    adivina = int(adivina)

    intentos = intentos + 1

    if adivina < numero:
        print('mi número es mayor')

    if adivina > numero:
        print('mi número es menor')

    if adivina == numero:
        break

if adivina == numero:
    intentos = str(intentos)
    print('Adivinaste, mi número era ' + numero)

if adivina != numero:
    numero = str(numero)
    print('No adivinaste, mi número era ' + numero)