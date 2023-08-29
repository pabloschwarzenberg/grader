#Juego adivina mi número
import random
numero = random.randint(1,20)
intentos = 0
jugando = True
while jugando:
    intentos += 1
    if intentos <= 5:
        eleccion = int(input('dime un numero:'))
        if eleccion == numero:
            print('Adivinaste, mi número era',numero)
            jugando = False
        elif eleccion > numero:
            print('mi numero es menor')
        elif eleccion < numero:
            print('mi numero es mayor')
    else:
        print('No adivinaste, mi número era',numero)
        jugando = False