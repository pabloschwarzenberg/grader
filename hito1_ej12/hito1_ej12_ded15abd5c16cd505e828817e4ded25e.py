#Juego adivina mi número
from random import randint
n=randint(1,21)
m=78
c=0
while m!=n and c<5:
    m=int(input("Adivina el numero entre el 1 y el 20"))
    if m==n:
          print("Adivinaste, mi numero era",n)
    else:
        c=c+1
        if m>n:
            print("Mi numero es mayor que ese")
        else:
            print("Mi numero es menor que ese")

if n!=m:
    print("No adivinaste, mi numero era",n)