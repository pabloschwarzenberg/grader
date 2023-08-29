#Juego adivina mi número
import random
numero_aleatorio = random.randrange(20)
ganaste = 0
for contador in range(5):
  numero_usario = int(input("Ingresa un numero del 1 al 20:"))
  if numero_usario > numero_aleatorio:
    print("mi numero es menor.")
  elif numero_usario < numero_aleatorio:
    print("mi número es mayor.")
  else:
    print("Adivinaste, mi número era", numero_aleatorio)
    ganaste += 1
    break

if ganaste == 0:
  print("No adivinaste, mi número era", numero_aleatorio)