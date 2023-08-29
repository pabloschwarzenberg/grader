#Juego adivina mi número
import random
numero = random.randint(1,20)
loops = 0
seguir = True 
while seguir:
  try:
    intento = int(input("Indica un numero: "))
  except EOFError:
    intento = 5
  if intento == numero:
    print("Adivinaste, mi numero era ",numero)
    seguir = False
  elif intento > numero:
    print("mi numero es menor")
  elif intento < numero:
    print("mi numero es mayor")
  if loops == 5:
    print("No adivinaste, mi numero era ",numero)
    seguir = False
  loops += 1