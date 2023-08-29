#Juego adivina mi número
import random

ns = (random.randint(1, 20))
print(ns)
n = int(input('Ingresa un numero que crees que sea:'))
contador = 1
while  n != ns:
    if n < ns:
        print('mi número es mayor')
        int(input('Ingresa un numero:'))
        contador = contador + 1

    elif n > ns:
        print('mi número es mayor')
        int(input('Ingresa un numero:'))
        contador = contador + 1

    elif contador == 5:
        print('No adivinaste, mi número era', ns)

    elif n == ns:
        print('Adivinaste, mi número era ', ns)
        