#Juego adivina mi número

from random import randrange

numero = randrange(1, 21)

ganar = False
contador = 0
while not ganar:
    adivinar = int(input('Elija un numero: '))
    if 1 <= adivinar <= 20:
        if adivinar < numero:
            contador += 1
            print('Mi numero es mayor')
            ganar = False
        elif adivinar > numero:
            contador += 1
            print('Mi numero es menor')
            ganar = False
        elif adivinar == numero:
            print('Adivinaste, mi numero era', numero)
            ganar = True
            break
    else:
        print('Solo numeros entre 1 y 20')
        ganar = False

    if contador == 5:
        print('No adivinaste, mi numero era', numero)
        break