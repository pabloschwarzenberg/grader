#Juego adivina mi número
import random

nrandom = random.randint(1,20)

n = int(input('Ingrese un número:'))

i = 0

while i < 4:
    if n > nrandom:
        print('mi número es menor')
        n = int(input('Ingrese un número:'))
    elif n < nrandom:
        print('mi número es mayor')
        n = int(input('Ingrese un número:'))
    i = i + 1
if n == nrandom:
        print('Adivinaste, mi número era', nrandom)
elif i == 4:
        print('No adivinaste, mi número era ', nrandom)     