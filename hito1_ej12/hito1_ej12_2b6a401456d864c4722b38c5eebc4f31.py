 #Juego adivina mi número
import random

intentos=5

print('¡Hola! ¿Cuál es tu nombre?')
nombre = input()

numero=random.randint(1,20)
print('Bueno, '+nombre+', piensa un número entre 1 y 20.')

while intentos<5:
    print ('¡Adivínalo! Tienes 5 intentos')
    adivina=input()
    adivinar=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Demasiado pequeño!')

    if adivina>numero:
        print('¡Demasiado grande!')

    if adivina==numero:
        break

if adivina==numero:
    intentos=str(intentos)
    print('Fabuloso, '+nombre+', acertaste el número en '+intentos+' intentos. ¡Estarás orgulloso!')

if adivina!=numero:
    numero=str(numero)
    print('¡Qué fatalidad '+nombre+' No adivinaste, mi numero era '+numero)
