#Juego adivina mi número
import random
numero_secreto=random.randint(1,20)
intentos=5
print("bienvenido al juego adivina mi numero")
print("estoy pensando en un numero del 1 al 20")
print("tienes 5 intentos para adivinarlo")

for i in range (intentos):
  print("intento",i+1)
  numero_adivinar=int(input("ingresa tu numero:"))
  
  if numero_adivinar<numero_secreto:
    print("mi numero es mayor")
  elif numero_adivinar>numero_secreto:
    print("mi numero es menor")
  else:
    print("adivinaste, mi numero era",numero_secreto)
    break
if numero_adivinar!=numero_secreto:
  print("no adivinaste, mi numero era",numero_secreto)