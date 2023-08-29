#Juego adivina mi número
import random

numero_secreto=random.randint(1, 20)
intentos=5
print("Adivina mi numero, tendras 5 intentos para adivinar mi numero entre el 1 y el 20")
while intentos>0:
  numero=int(input("Ingrese un numero entre el 1 al 20: "))
  if numero==numero_secreto:
    print("Adivinaste, mi número era {}".format(numero_secreto))
    break
  elif numero>numero_secreto:
    print("Mi numero es menor...")
    intentos-=1
    print("Te quedan {} intentos".format(intentos))
  else:
    print("Mi numero es mayor...")
    intentos-=1
    print("Te quedan {} intentos".format(intentos))
    
if intentos==0:
  print("No has podido adivinar mi numero, era", numero_secreto)     