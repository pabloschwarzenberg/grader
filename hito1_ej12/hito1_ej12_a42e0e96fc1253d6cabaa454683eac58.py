#Juego adivina mi número
import random
a=random.randint(1,20)

contador=0
while True:
    ingrese=int(input())
    contador+=1
    if contador!=5:
        if ingrese<a:
            print('El numero es mayor')
        elif ingrese>a:
            print('El numero es menor')
        elif ingrese==a:
            print('Adivinaste, mi numero era',a)
            break
    else:
        print('No adivinaste, mi numero era',a)
        break    

