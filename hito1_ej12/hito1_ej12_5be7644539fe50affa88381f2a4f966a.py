#Juego adivina mi número
from random import randint
n = randint(1,20)
contador = 0
adivinar = int(input("Ingrese un valor: "))
while n != adivinar and contador < 5:
  if adivinar < n:
    print("mi numero es mayor")
    adivinar = int(input("Ingrese un valor: "))
  else:
    print("mi numero es menor")
    adivinar = int(input("Ingrese un valor: "))
  contador = contador + 1
if contador == 5:
    print( "No adivinaste, mi número era: ", n)
if adivinar == n:
    print("Adivinaste, mi número era: ", n) 