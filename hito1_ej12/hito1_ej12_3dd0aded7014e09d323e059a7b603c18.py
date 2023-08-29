#Juego adivina mi número
import random
numero_secreto=random.randint(1,20)
contador=0
while contador<=4:
  numero=int(input("Ingrese un numero entre el 1 y el 20, para asi adivinar el numero secreto: "))
  if numero<numero_secreto:
    contador=+1
    print("El numero ingresado es menor que el numero secreto.")
    
  elif numero_secreto<numero:
    contador=+1
    print("El numero ingresado es mayor al numero secreto.")
    
  elif numero_secreto==numero:
    print("Adivinaste, mi numero era: ",numero)
    break
if contador == 5:
  print("No adivinaste, mi numero era: ",numero_secreto)
  