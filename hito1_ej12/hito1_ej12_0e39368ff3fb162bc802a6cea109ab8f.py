#Juego adivina mi número
import random
import sys
a=random.randint(1,20)
print(a)
i=0
while (i<5):
    b=int(input())
    if b<a:
        print("Su numero es menor a mi numero")
        i=i+1
    elif b>a:
        print("Su numero es mayor a mi numero")
        i=i+1
    else:
        print("Adivinaste, mi numero era", a)

if i==5:
    print("No adivinaste, mi numero era", a)