#Juego adivina mi número
import random
numeros = random.randint(1,20)
num = int(input('Ingrese el numero a adivinar: '))
intentos = 0

while intentos < 5:
    intentos+=1
    
    
    if num > numeros:
        print('mi número es menor')
    elif num < numeros:
        print('mi número es mayor')
    if num == numeros:
        break
if num == numeros:
    print('Adivinaste, mi número era',numeros,) 
else:
    print('No adivinaste, mi número era',numeros,)