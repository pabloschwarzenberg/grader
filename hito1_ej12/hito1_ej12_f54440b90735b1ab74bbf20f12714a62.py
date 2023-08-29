#Juego adivina mi número
import random

num_aleatorio = random.randint(1, 20)
#print(num_aleatorio)

aux = False
intentos = 1


numero = int(input("Ingrese su numero: "))
while aux != True:
  if intentos == 5:
    print("No adivinaste, mi numero era: ", num_aleatorio)
    break
  elif numero == num_aleatorio:
    print("Adivinaste, mi numero era: ", num_aleatorio)
    aux = True
  elif numero < num_aleatorio:
    print("Mi numero es mayor")
    intentos += 1
    numero = int(input("Intentalo otra vez: "))
    
  elif numero > num_aleatorio:
    print("Mi numero es menor")
    intentos += 1
    numero = int(input("Intentalo otra vez: "))
    