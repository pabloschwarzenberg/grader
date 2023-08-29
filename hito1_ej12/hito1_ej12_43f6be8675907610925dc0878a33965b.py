#Juego adivina mi número
import random  
a=random.randint(1,20)
adivino = False
cont=0
while not adivino and cont < 5:
  n=int(input())
  if a==n:
    adivino= True
    print("Adivinaste mi numero era",n)
  elif a!=n and a<n:
    cont=cont+1
    print("No adivinaste, pero mi numero es mayor que",n)
  elif a!=n and a>n:
    cont=cont+1
    print("No adivinaste, pero mi numero es menor que",n)
if not adivino:
  print ("No adivinaste, minumero era",a)