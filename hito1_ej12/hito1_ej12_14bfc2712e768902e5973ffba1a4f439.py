#Juego adivina mi número
import random
intentos=0
a = random.randint(1, 20)
while(1):
    if intentos == 5:
        print('No adivinaste, mi número era ', a)
        break
    b=int(input('Que numero crees que es?'))
    if a == b:
        print('Adivinaste, mi número era ', a)
        break
    elif a>b:
        print('mi numero es mayor')
        intentos+=1
    elif b>a:
        print('mi numero es menor')
        intentos += 1