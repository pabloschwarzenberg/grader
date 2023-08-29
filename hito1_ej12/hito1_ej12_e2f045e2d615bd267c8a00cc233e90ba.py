#Juego adivina mi número
import random

x = random.randint(1, 20)
count_error = 0

while count_error < 5:
    print('Intenta adivinar mi numero')
    a = int(input('Ingresa un numero: '))

    if a == x:
        print('Adivinaste, mi numero era'+str(x))
        break
    elif a < x:
        print('Mi numero es mayor')
    elif a > x:
        print('Mi numero es menor')
    
    count_error+= 1

if count_error == 5:
    print('No adivinaste, mi numero era: '+str(x))     