#Juego adivina mi número
import random
x=random.randrange(20)
i=0
while i <5:
    y=int(input('Ingresa un número de 1 a 20: '))
    if y==x:
        print('Adivinaste, mi número era',x)
        i=4
    elif y>x:
        print('Mi número es menor')
    
    elif y<x:
        print('Mi número es mayor')
        
    elif i==4:
        print('No adivinaste, mi número era:',x)
    
    i=i+1       