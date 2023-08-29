#Juego adivina mi número
from random import randint
numero = randint(1,20)
intentos = 1
while intentos<=5:
  numero_jugador = int(input("¿Cual es mi número?:"))
  intentos += 1
  if numero_jugador==numero:
    print("Adivinaste, mi número era",numero)
    break
  elif numero>numero_jugador:
    print("mi número es mayor")
  elif numero<numero_jugador:
   print("mi número es menor")
  if intentos>5:
    print("No adivinaste, mi número era",numero)