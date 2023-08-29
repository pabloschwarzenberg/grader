#Juego adivina mi número
import random
número=random.randint(1,20)
a=0
while a<=5:
    Op=int(input('Adivina mi número: '))
    a=a+1
    if número==Op:
            print('Adivinaste, mi número era', número)
            break
    elif número>Op:
            print('El número que elegiste es menor')
    elif número<Op:
            print('El número que elegiste es mayor')
if a>5:
    print("No adivinaste, mi número era", número)
          