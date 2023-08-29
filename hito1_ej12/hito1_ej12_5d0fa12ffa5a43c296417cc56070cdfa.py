import random

secreto = random.randint(1,20)

intentos = 5
contador = 1

n = int(input('ingrese un numero entre 1 y 20: '))

while(intentos>contador):

    if (secreto < n):
        print('mi número es menor')
        n = int(input('ingrese un numero entre 1 y 20: '))

    else:
        print('mi número es mayor')
        n = int(input('ingrese un numero entre 1 y 20: '))

    if (secreto == n):
        print('Adivinaste, mi número era', secreto)
        break

    contador = contador+1

if(contador == 5):
    print('No adivinaste, mi número era', secreto)