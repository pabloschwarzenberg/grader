#Juego adivina mi número
import random

numero_de_intentos = 0
numero_minimo = 1
numero_maximo = 20

numero_secreto = random.randint(numero_minimo, numero_maximo)

while numero_de_intentos < 6:
     print("Elije un número: ")
     numero = input()
     numero = int(numero)
     numero_de_intentos = numero_de_intentos + 1
     
     if numero < numero_secreto:
       print("Mi número es mayor")
     if numero > numero_secreto:
       print("Mi número es menor")
     if numero == numero_secreto:
       break
       
if numero == numero_secreto:
  print("Adivinaste, mi número era " + str(numero_secreto))
if numero != numero_secreto:
  print("No adivinaste, mi número era " + str(numero_secreto))