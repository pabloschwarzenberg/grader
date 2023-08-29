#Juego adivina mi número
import random
x=random.randint(1,20)
intentos=0
while intentos<5:
  respuesta=int(input())
  if respuesta<x:
    n=intentos+1
    print("el numero es menor a ese")
    intentos=n
  elif respuesta>x:
    n=intentos+1
    print("el numero es mayor a ese") 
    intentos=n
  elif respuesta==x:
    n=intentos+1
    print("Adivinaste, mi número era " +str(x))
    intentos=n
print("No adivinaste, mi número era " +str(x))



