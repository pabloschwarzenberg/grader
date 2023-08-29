#Juego adivina mi número
import random
x=random.randint(1,20)
i=0
while i<5:
     n=int(input("Numero: "))
     if n>x:
          print("mi número es menor")
     if n<x:
          print("mi número es mayor")
     if n==x:
          print("Adivinaste, mi número era",n)
     i=i+1
print("No adivinaste, mi número era ",x)      