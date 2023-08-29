#Juego adivina mi número
import random

intentos=0

numero=random.randint(1,20)
print('Piensa en un número entre 1 y 20.')

while intentos<5:
    ADIVINA=input()
    ADIVINA=int(ADIVINA)

    intentos=intentos+1

    if ADIVINA<numero:
        print ('mi número es mayor')

    if ADIVINA>numero:
        print('mi número es menor')

    if ADIVINA==numero:
        break

if ADIVINA==numero:
    print('Adivinaste, mi número era '+ str(numero))

if ADIVINA!=numero:
    print("No adivinaste, mi número era "+ str(numero))         