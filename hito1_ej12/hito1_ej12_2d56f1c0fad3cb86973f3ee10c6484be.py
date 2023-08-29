#Juego adivina mi número
import random
intentos=5
numero=random.randint(1,20)
while 0<intentos:
  n=int(input("ingrese numero:"))   
  if n<numero:
      print("muy bajo")
  if numero<n:
      print("muy alto")
  if n==numero:   
   break
  intentos=intentos-1 
if n==numero:
  print("Adivinaste mi número era",numero)
if n!=numero:
  print("No adivinaste, mi número era",numero)
  