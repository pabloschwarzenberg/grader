#Juego adivina mi número
import random

n=random.randint(1,20)
i=0
while i<5:
  x=int(input("Adivina mi número: "))
  if x==n:
    print("Adivinaste, mi número era",n)
    break
    
  else:
    i=i+1
    if x<n:
      print("Mi número es un poco mayor... inténtalo de nuevo.")
    else:
      print("Mi número es más pequeño... inténtalo de nuevo.")

if i==5:
  print("No adivinaste, mi número era ",n,)
      