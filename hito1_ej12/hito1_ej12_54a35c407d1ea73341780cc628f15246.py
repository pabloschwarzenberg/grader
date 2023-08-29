#Juego adivina mi número
import random
x=random.randint(1,20)
numero=int(input('adivina un numero del 1 al 20: '))
i=1
while i<5:
    if numero==x:
        print('Adivinaste, mi numero era',x)
        break
    elif numero>x:
        print('mi numero es menor')
        numero=int(input('adivina un numero del 1 al 20: '))
    else:
        print('mi numero es mayor')
        numero=int(input('adivina un numero del 1 al 20: '))
    i=i+1
if i==5:
    print('no adivinaste, mi numero era',x)      