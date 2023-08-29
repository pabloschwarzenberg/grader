#Juego adivina mi número
import random

n = random.randint(1,20)
i = 0
adivino = 0
while i < 5:
  adivino = int(input("Ingresa tu intento: "))
  if adivino == n:
    break
  elif adivino < n:
    print ("mi número es mayor")
    i += 1
  elif adivino > n:
    print("mi número es menor")
    i += 1
if adivino == n:
  print("Adivinaste, mi número era", n)
else:
  print("No adivinaste, mi número era", n)