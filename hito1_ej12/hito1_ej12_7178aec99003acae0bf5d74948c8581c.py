#Juego adivina mi número
import random
x=random.randint(1,20)
intentos=0
y=0 
while y!=x and intentos!=5:
  y=int(input())
  if y==x:
    print("Adivinaste, mi numero era ", x)
  if y<x:
    print("mi nùmero es mayor")
    intentos=intentos+1
  if y>x:
   print("mi nùmero es menor")
   intentos=intentos+1
if intentos==5:
  print("No adivinaste, mi nùmero era ", x)