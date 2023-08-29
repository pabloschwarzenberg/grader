#juego adivina mi numero
from random import randint

NumeroparaAdivinar = randint(1,20)

intentos = 0
NumeroAdivinado = 0

while intentos <= 5:
    if intentos > 1:
        NumeroAdivinado = int(input('intenta de nuevo: '))
    else:
        NumeroAdivinado = int(input('digita el numero que quieres elegir: '))

    intentos += 1
    if NumeroAdivinado == NumeroparaAdivinar:
        print('adivinaste mi numero era',NumeroparaAdivinar)
        break
    if NumeroparaAdivinar > NumeroAdivinado:
        print('mi número es mayor')
    else:
        print('mi número es menor')

    if intentos == 5:
        print('no adivinaste mi numero era',NumeroparaAdivinar)
        break
        