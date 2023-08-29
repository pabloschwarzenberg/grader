#Juego adivina mi número
from random import randrange

i=1
n=randrange(100)
intento=0
while i==1:
 x=int(input("Número:"))

 if x==n:
        intento+=1
        print("Adivinaste, mi numero era",n)
        i=0
 elif x<n:
        print("Mi numero es mayor")
        intento+=1
 elif x>n:
        print("Mi numero es menor")
        intento+=1
 if intento==5:
        print("No adivinaste, mi numero era",n)
        i=0