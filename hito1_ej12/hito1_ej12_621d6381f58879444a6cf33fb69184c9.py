#Este es un juego de adivinar el número
import random

intentos=0

print('¡Hola! ¿Cuál es tu nombre?')
nombre = input()

numero=random.randint(1,20)
print('Bueno, '+nombre+', piensa un número entre 1 y 20.')

while intentos<5:
    print ('¡Adivínalo! Tienes 5 intentos')
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Demasiado pequeño!')

    if adivina>numero:
        print('¡Demasiado grande!')

    if adivina==numero:
        break

if adivina==numero:
    print("Adivinaste, mi numero era:"+numero)

if adivina!=numero:
    numero=str(numero)
    print('No adivinaste, mi numero era: '+numero)