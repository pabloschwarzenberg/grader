#Juego adivina mi número

import random
x=random.randint(1,20)

y=int(input('ingresa numero'))
contador=0
t=True
while t:
    if y==x:
        print('adivinaste, mi numero era' , x )
        break
    elif y!=x:
        if contador==5:
                print(' No adivinaste, mi número era', x)
                break
        if y>x:
            print('el numero es menor')
            contador+=1
    
        if y<x:
            print('el numero es mayor')
            contador+=1
                  
        