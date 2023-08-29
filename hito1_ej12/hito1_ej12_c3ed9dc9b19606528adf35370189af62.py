#Juego adivina mi número
import random
numero_aleatorio=random.randint(1,20)
intentos=5
for i in range(0,5):
  n=int(input())
  if n==numero_aleatorio:
    print("Adivinaste, mi número era {}".format(numero_aleatorio))
    break
  elif n>numero_aleatorio:
    print("mi número es menor")
  elif n<numero_aleatorio:
    print("mi número es menor")
  intentos-=1
if intentos==0:
  print("No adivinaste, mi número era {}".format(numero_aleatorio))
  