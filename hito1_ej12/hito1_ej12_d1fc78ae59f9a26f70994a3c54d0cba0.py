#Juego adivina mi número
import random
i=0
a= random.randint(1,21)

while i<6:
     n= int(input())
     if n==a:
        print("Adivinaste, mi número era",n)
        break
     elif n>a:
        i=i+1
        print("el número ingresado es mayor")
     elif n<a:
        i=i+1
        print("el número ingrsado es menor")
if i==6:
   print("No adivinaste, mi número era",n)
     