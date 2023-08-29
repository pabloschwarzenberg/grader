#Juego adivina mi número
from random import randint
contador=1
Numero_random=randint(1,20)

while True:
  Numero_Usuario=int(input("Ingresa un numero"))

  if Numero_Usuario==Numero_random:
    print("Adivinaste, mi número era ",Numero_random)
    break
  elif Numero_Usuario!=Numero_random and contador==5:
    print("No adivinaste, mi número era ",Numero_random)
    break
  elif Numero_Usuario!=Numero_random and Numero_random<Numero_Usuario:
    print("Mi número es menor")
    contador=contador+1
    continue
  elif Numero_Usuario!=Numero_random and Numero_random>Numero_Usuario:
    print("Mi número es mayor")
    contador=contador+1
    continue   