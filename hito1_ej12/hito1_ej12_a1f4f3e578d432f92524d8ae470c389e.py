#Juego adivina mi número
from random import randrange
n_random=(randrange(20))
for x in range(5):
  n_1=int(input("ingresa un numero"))
  if n_1==n_random:
    print("Adivinaste, mi número era", n_random)
    break
  if n_1>n_random:
    print("mi número es menor")
  if n_1<n_random:
    print("mi número es mayor")
  if x==4:
    print("No adivinaste, mi número era ", n_random)
      