#juego adivina mi numero
import random

numerointentos = 0
numeroMIN = 1
numeroMAX = 20

numeroaleatorio = random.randint(numeroMIN, numeroMAX)

#blucle juego
while numerointentos < 5:
    numero = int(input('dame un numero: '))
    numerointentos = numerointentos + 1

    if numero < numeroaleatorio:
        print('mi número es mayor')
    if numero > numeroaleatorio:
        print('mi número es menor')
    if numero == numeroaleatorio:
        break

if numero != numeroaleatorio:
    print('No adivinaste, mi número era ', numeroaleatorio)

if numero == numeroaleatorio:
    print('Adivinaste, mi número era ', numeroaleatorio)
