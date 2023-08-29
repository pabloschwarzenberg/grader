#Juego adivina mi número
import random
intentos=5
while intentos>0:
  numero=random.randint(1,20)
  numero_elegido=int(input())
  if numero>numero_elegido:
    print("mi número es mayor")
    intentos=intentos-1
  elif numero<numero_elegido:
    print("mi número es menor")
    intentos=intentos-1
  else:
    print("Adivinaste, mi número era ",numero)          
    break
if intentos==0:
    print("No adivinaste, mi número era ",numero)