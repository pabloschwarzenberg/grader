#Juego adivina mi número
from random import randint 

secreto = randint(1, 21)

i = 1
while i <= 5:

    ingreso = int(input())

    if ingreso < secreto:
        print('mi número es menor')
    
    elif ingreso > secreto:
        print('mi número es mayor')
    
    elif ingreso == secreto:
        print('Adivinaste, mi número era ' + str(secreto))
        break

    i += 1

if i > 5:
    print('no adivinaste, mi número era ' + str(secreto))      