#Juego adivina mi número
import random
numero_secreto=(random.randint(1, 20))

intentos=0
while intentos<4:
  jugada=int(input("adivina el número secreto"))
  intentos = intentos +1
  if jugada > numero_secreto:
    print ("tu número es mayor que el número secreto")
  elif jugada < numero_secreto:
    print ("tu número es menor que el número secreto")

  if jugada == numero_secreto:
    break

if jugada == numero_secreto:
  print ("Adivinaste, mi número era", numero_secreto)
  
else:
  print("No adivinaste, mi número era ", numero_secreto)