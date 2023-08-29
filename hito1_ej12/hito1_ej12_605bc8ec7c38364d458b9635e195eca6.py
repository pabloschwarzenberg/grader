#Juego adivina mi número
import random

intentos=0
n=random.randint(1,20)

while intentos < 5:
  intentos=intentos+1
  print("Elige un numero del 1 al 20")
  numero= input()
  numero=int(numero)
  if numero < n:
    print("mi numero es menor")
  if numero > n:
    print("mi numero es mayor")
  if numero == n:
    break

if numero == n:
 print("Adivinaste, mi numero era",n)
else:
 numero != n
 print("No adivinaste , mi numero era",n)     