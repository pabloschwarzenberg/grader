#Juego adivina mi número
from random import randint
n=randint(0,21)
i=0
while i<5:
 x=int(input("Trate de adivinar el numero"))
 if x<n:
  print("Mi numero es mayor")
  i=i+1
 elif x>n:
  print("Mi numero es menor")
  i=i+1
 elif x==n:
  print("Adivinaste,mi número era",x)
  break
if i==4 and x!=n:
 print("No adivinaste, mi número era",n)
 