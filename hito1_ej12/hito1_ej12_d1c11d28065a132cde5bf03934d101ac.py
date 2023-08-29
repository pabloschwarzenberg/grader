#Juego adivina mi número
import random

intentos=0

numero=random.randint(1,20)
print('Piensa un número entre 1 y 20.')

while intentos<5:
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1

    if adivina<numero:
        print ('mi número es mayor')

    if adivina>numero:
        print('mi número es menor')

    if adivina==numero:
        break

if adivina==numero:
    print('Adivinaste, mi número era '+ str(numero))

if adivina!=numero:
    print("No adivinaste, mi número era "+ str(numero))      