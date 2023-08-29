# Este es el juego de adivinar el número.

import random


intentosRealizados = 0


número = random.randint(1, 20)

print('estoy pensando en un número entre 1 y 20.')



while intentosRealizados < 5:

        print('Intenta adivinar.') 

        estimación = input()

        estimación = int(estimación)



        intentosRealizados = intentosRealizados + 1



        if estimación < número:

            print('Mi numero es mayor') 



        if estimación > número:

            print('Mi numero es menor')



        if estimación == número:

            break



if estimación == número:

    intentosRealizados = str(intentosRealizados)

    print('Adivinaste, mi numero era: ',número)



if estimación != número:

    número = str(número)

    print('No adivinaste, mi numero era: ' + número)
      