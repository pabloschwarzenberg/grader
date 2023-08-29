#Juego adivina mi número
import random
numero_secreto=random.randint(1,20)
i=0
while i<5:
  n=int(input("Ingrese un numero: "))
  if n>numero_secreto:
    print("mi numero es mayor")
  elif n<numero_secreto:
    print("mi numero es menor")
  else:
    break
  i+=1
if n==numero_secreto:
  print("Adivinaste,mi numero era",numero_secreto)
if i==5:
  print("No adivinaste, mi numero era",numero_secreto)