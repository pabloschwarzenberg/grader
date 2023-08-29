#Juego adivina mi número
import random

numero=random.randint(1,20)

intentos=0



while intentos < 5:
  global numero
  
  n=int(input())
  
  if n < numero:
    print("mi número es mayor")
    intentos=intentos+1
  elif n > numero:
    print("mi número es menor")
    intentos=intentos+1
  elif n== numero:
    print("Adivinaste,mi número era ",numero)
    break

if intentos==5:
  print("No adivinaste, mi número era ",numero)