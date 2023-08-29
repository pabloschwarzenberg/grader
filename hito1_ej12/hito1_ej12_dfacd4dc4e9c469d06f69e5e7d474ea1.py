#Juego adivina mi número
import random

adv=random.randint(1,20)
a=int(input('ingrese numero: '))
i=0
while a!=adv and i<5:
    if a>adv:
        print('mi numero es menor')
    else:
        print('mi numero es mayor')
    i = i + 1
    if i<5:
        a = int(input('ingrese numero: '))

if a==adv and i<5:
    print('Adivinaste, mi numero era', adv)
else:
    print('No adivinaste, mi numero era', adv)