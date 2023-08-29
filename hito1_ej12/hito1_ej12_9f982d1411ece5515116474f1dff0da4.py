#Juego adivina mi número
from random import randint



numero = randint(1, 20)

intentos = 1

while intentos < 6:

    adivina = int(input('Adivina el numero (entre 1 y 20): '))

    if adivina < numero:

        print('Mi numero es mayor')

        intentos += 1

    elif adivina > numero:

        print('Mi numero es menor')

        intentos += 1

    else:

        print('Adivinaste, mi numero era: %i' % numero)

        break

else:

    print('No adivinaste, mi numero era: %i' % numero)