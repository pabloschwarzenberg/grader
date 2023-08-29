#Juego adivina mi número
import random
n=random.randint(1,20)
intentos=5
while intentos>0:
    nj=int(input("ingrese un número "))
    if nj==n:
        print("Adivinaste, mi número era ",n)
        break
    elif nj<n:
        print("numero muy PEQUEÑO")
    elif nj>n:
        print("numero muy GRANDE")
    intentos-=1
    print("te quedan ", intentos," Intentos")
if intentos==0:
    print("No adivinaste, mi número era ",n)