#Juego adivina mi número
import random
x=random.randrange(0,20)
n = int(input('Ingrese su numero: '))

for i in range(5):
    if n < x:
        print('mi numero es mayor')
    elif n > x:
        print('mi numero es menor')
    elif n == x:
        print('Adivinaste, mi numero era: ',n)
    else:
            i=i+1
            print('No adivinaste, mi numero era: ',n)
            break