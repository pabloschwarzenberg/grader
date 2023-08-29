#Juego adivina mi número
from random import*


x= randint(1,20)
print(x)
a=int(input('ingrese el numero:'))
contador=1
while contador<=5:
    if x==a:
        print('Adivinaste, mi número era', x)
        break
    elif contador==5:
        print('No adivinaste, mi número era', x)
        break
    elif a>x:
        print('mi número es menor')
        contador+=1
        a=int(input('ingrese el numero:'))
    elif a<x:
        print('mi número es mayor')
        contador+=1
        a=int(input('ingrese el numero:'))      