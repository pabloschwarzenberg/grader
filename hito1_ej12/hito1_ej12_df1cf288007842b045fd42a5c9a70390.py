#Juego adivina mi número
import random

n = random.randrange(1, 21)
intento = 5

while intento > 0:
    numero = int(input())
    
    if numero > n:
        print('mi número es menor')
        
    elif numero < n:
        print('mi número es mayor')   
        
    else:
        print('Adivinaste, mi número era', n)
        break
    
    intento -= 1
    
if intento == 0:
    print('No adivinaste, mi número era', n)

