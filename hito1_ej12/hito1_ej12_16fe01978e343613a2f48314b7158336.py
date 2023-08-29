#Juego adivina mi número
import random
n = random.randint(1,20)
i = 0
while i<5:
     a = int(input("Ingrese un número entre 1 y 20:"))
     if(a<n) or (a>n):
           print("a es mayor a n",a>n)
           print("a es menor a n",a<n)
     i = i + 1
     if(i==4):
           print("No a adivinaste, mi numero era",n)
           break
     if(a==n):
           print("Adivinaste,mi numero era",n)
           break
           

           