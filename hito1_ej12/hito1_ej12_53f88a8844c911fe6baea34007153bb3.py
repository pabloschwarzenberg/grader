#Juego adivina mi número
from random import randint

a=randint(1,20)
n=int(input("numero: "))
p=0
while n!=a:
    if n>a:
        print("tu número es mayor al número secreto")
        n=int(input("numero: "))
        p=1+p
    if n<a:
        print("tu número es menor al número secreto")
        n=int(input("número: "))
        p=1+p

if p==5:
    print("No adivinaste, mi número era",a)

elif n==a:
    print("Adivinaste, mi número era",a)