#Juego adivina mi número
import random
x=random.randint(1,20)
cont=0
while cont<5:
    a=int(input('adivina el numero: '))
    if a>x:
        print('mi numero es mayor')
    if a<x:
        print('mi numero es menor')
    if a==x:
        print('Adivinaste, mi número era', a)
    cont=cont+1 
print('no adivinaste, mi número era', x)