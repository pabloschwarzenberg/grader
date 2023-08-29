#Juego adivina mi número
Intentos=5

import random
n=random.randint(1,20)

while Intentos>0:
    N=int(input("intenta adivinar mi numero:"))
    if (N==n):
        print('Adivinaste, mi numero era',n)
        break
    
    elif (N>n):
        print('tu numero es mayor')
        Intentos=Intentos-1
    elif (N<n):
        print('tu numero es menor')
        Intentos=Intentos-1
if (Intentos==0):
    print('No adivinaste, mi numero era',n)
      