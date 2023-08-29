#Juego adivina mi número
import random

intentos = 5 
n = random.randint(1,20)
while intentos>0:
  adivina = int(input("Ingresa para adivinar"))
  if n>adivina:
    print("Mi número es mayor")
    intentos-=1
  elif n<adivina:
    print("Mi número es menor")
    intentos-=1
  elif n == adivina:
    print("Adivinaste, mi número era",n)

print("No adivinaste, mi número era", n)     