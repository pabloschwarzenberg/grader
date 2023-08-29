#Juego adivina mi número
import random
oportunidades=5
numero_aleatorio=random.randint(1,20)
while oportunidades>0:
  n=int(input())
  if numero_aleatorio<n:
    print("mi numero es menor")
  elif numero_aleatorio>n:
    print("mi numero es mayor")
  oportunidades-=1
if oportunidades==0:
  if n==numero_aleatorio:
    print("Adivinaste, mi numero era",numero_aleatorio)
  else:
    print("No adivinaste, mi numero era",numero_aleatorio)