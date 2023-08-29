#Juego adivina mi número
import random
print("Adivina mi numero, tienes 5 intentos")
numero_secreto = random.randint(1, 20)
intentos = 0
while intentos < 5:
  numero_ingresado = int(input("Ingresa el numero: "))
  intentos += 1
  if numero_ingresado > numero_secreto:
    print("Mi numero es menor")
  if numero_ingresado < numero_secreto:
    print("Mi numero es mayor")
  if numero_ingresado == numero_secreto:
    print("Adivinaste")
    break
else:
  print("No adivinaste, mi numero era: " + str(numero_secreto))