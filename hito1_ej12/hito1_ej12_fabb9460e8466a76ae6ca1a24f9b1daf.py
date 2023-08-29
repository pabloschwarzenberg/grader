#Juego adivina mi número
import random
NumeroS=random.randrange(21)
intentos=5
v=False
while intentos!=0:
  guess=int(input("Que numero tengo? "))
  if guess==NumeroS:
    print("Adivinaste, mi número era",NumeroS)
    v=True
    break
  elif guess>NumeroS:
    print("mi número es menor")
    intentos=intentos-1
  elif guess<NumeroS:
    print("mi número es mayor")
    intentos=intentos-1
if v==False:
  print("No adivinaste, mi número era",NumeroS)
