#Juego adivina mi número
import random as rd

numero = rd.randint(1,20)

for intentos in range(5):
    ingreso = int(input('Adivina el numero: '))
    if ingreso > numero:
        print('mi número es es menor')
    elif ingreso < numero:
        print('mi número es es mayor')
    elif ingreso == numero:
        print('Adivinaste, mi número era ',numero)
        break
if numero != ingreso:
    print('No adivinaste, mi número era', numero)

    