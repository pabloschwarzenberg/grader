#Juego adivina mi número
import random

intentos=0


numero = random.randint(1,20)
print('piensa un número entre 1 y 20')

while intentos<5:
    adivina = input()
    adivina = int(adivina)

    intentos = intentos+1
   
    if adivina>numero:
        print ('mi numero es menor')

    if adivina<numero:
        print('mi numero es mayor ')

    if adivina == numero:
        break

if adivina==numero:
    numero = str(numero)
    print('Adivinste, mi numero era ' +numero)

else:
    adivina!=numero
    numero = str(numero)
    print('No adivinaste, mi numero era ' +numero)

      