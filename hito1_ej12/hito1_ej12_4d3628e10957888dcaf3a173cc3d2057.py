#Juego adivina mi número
import random

numero = random.randint(1,20)
intentos = 0

jugando = True

print('Adivina un numero del 1 al 20: ')

while jugando:

    intentos += 1
    if intentos <= 5 :
        eleccion = int(input('Dime un numero: '))
        if eleccion == numero:
            print('Has acertado, mi numero era: ', numero)
            jugando = False
        elif eleccion > numero:
            print('Mi numero es menor')
        elif eleccion < numero:
            print('Mi numero es mayor')
    else:
        print('No adivinaste, mi numero era: ', numero)
        jugando = False