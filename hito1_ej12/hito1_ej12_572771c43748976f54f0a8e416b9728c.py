#Juego adivina mi número
from random import *
nr = randint(1,20)
intentos = 0
while intentos <6:
  n = int(input("Ingrese un numero: "))
  if n>nr :
    print("mi número es menor")
    intentos += 1
  elif n<nr :
    print("mi número es mayor")
    intentos += 1
  elif n == nr:
    print("Adivinaste, mi número era", nr)
    break
  if intentos == 5 :
    print("No adivinaste, mi número era ",nr)
    break
    