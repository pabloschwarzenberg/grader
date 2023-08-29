#Juego adivina mi número
import random
intentos=5
x=random.randint(1,20)
no_adivina=True
while no_adivina and intentos>0:
    n=int(input())
    if n!=x:
      intentos=intentos-1
      if n<x:
          print("Tu número es menor")
      if n>x:
          print("Tu número es mayor")
      no_adivina=True
    else:
        print("Adivinaste, mi número era",x)
        no_adivina=False
if intentos==0:
    print("No adivinaste, mi número era",x)