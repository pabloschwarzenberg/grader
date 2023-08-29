#Juego adivina mi número
import random

n=random.randint(1, 20)
print(n)
c=0
while c<5:
    s=int(input("ingrese un numero"))
    if s==n:
        print ("Adivinaste, mi número era ",n)
        break
    if s<n:
        print("mi número es mayor")
        c=c+1
    if s>n:
        print ("mi número es menor")
        c=c+1
if c>=5:
    print("No adivinaste, mi número era",n)