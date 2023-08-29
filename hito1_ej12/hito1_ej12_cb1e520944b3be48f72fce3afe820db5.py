#Juego adivina mi número
import random
import math
a=1
b=20
c=1
m=random.randint(a,b)
print('Tengo un numero en mente entre 1 y 20. Adivina cual es')
while c<6:
    d = int(input('Tu piensas que es: '))
    if d == m:
        print('Adivinaste, mi número era', m)
        break
    if d >=21 or d<1:
        print('Esta fuera de rango')
        c = c+1
        continue
    if d > m:
        print('Es menor')
        c=c+1
        continue
    if d < m:
        print(' Es mayor')
        c =c+1
        continue
if c>=6:
    print('No adivinaste, mi número era',m)      