#Juego adivina mi número
import random
x = random.randint(1,20)

for i in range(5):
    y = int(input(''))
    if y == x:
        print('Adivinaste, mi número era', x)
        y = 0
        break
    elif y > x:
       print('mi número es menor') 
    elif y < x:
       print('mi número es mayor') 

if y != 0:
    print('No adivinaste, mi número era ', x)
          