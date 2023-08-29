#Juego adivina mi número
import random
ns = random.randint(1,20)
for Intento in range(5):
  Numero = int(input())
  if Numero == ns:
    print("Adivinaste, mi número era"+str(ns))
    break
  elif Numero > ns:
    print("mi número es mayor")
  elif Numero < ns:
    print("mi número es menor")
  if Intento == 4:
     print("No adivinaste, mi número era "+str(ns))