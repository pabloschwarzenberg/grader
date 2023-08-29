#Juego adivina mi número
import random

x= random.randint(1, 20)

i=5

while i!= 0:   
    n= int(input('numero: '))
    if n== x:
        print('Adivinaste, mi número era', x)
        break
    if n< x:
        print('mi número es mayor')
        i=i-1
    else:
        print('mi número es menor')
        i=i-1

if i== 0:
    print('No adivinaste, mi número era', x)
