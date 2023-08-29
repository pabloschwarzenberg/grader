#Juego adivina mi número
import random
contador=5
l=random.randint(1,20)
while contador>0:
    n=int(input('elige un numero :'))
    if n<l:
        print('te equivocaste, el numero es mayor')
        contador=contador-1
    elif n>l:
        print('te equivocaste, el numero es menor')
        contador=contador-1
    elif n==l:
        print('adivinaste mi numero era',l)
    elif n!=l:
        print('no adivinaste, mi numero era',l)
        contador=contador-1
      