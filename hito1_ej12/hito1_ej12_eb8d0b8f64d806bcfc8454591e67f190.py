#Juego adivina mi número
from random import randint
n=randint(1,20)
intentos=5
while intentos!=0:
    m=int(input("Adivina mi numero"))
    if m>n:
        print("Mi numero es menor")
        intentos-=1
        continue
    if n>m:
        print("Mi numero es mayor")
        intentos-=1
        continue
    if n==m:
        print("Adivinaste, mi número era",n)
        break
if intentos==0:
    print("No adivinaste, mi número era",n)