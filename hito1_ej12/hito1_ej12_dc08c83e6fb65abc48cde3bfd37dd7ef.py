#Juego adivina mi número
import random
numero_adivinar=random.randint(1,20)
intentos=0
while intentos<5:
  num=int(input())
  if num==numero_adivinar:
      break
  if num<numero_adivinar:
      print ("mi numero es mayor")
  if num>numero_adivinar:
      print("mi numero es menor")
  intentos=intentos+1
if num!=numero_adivinar:
    print("No adivinaste, mi numero era ",numero_adivinar)
if num==numero_adivinar:
    print("Adivinaste, mi numero era ", numero_adivinar)