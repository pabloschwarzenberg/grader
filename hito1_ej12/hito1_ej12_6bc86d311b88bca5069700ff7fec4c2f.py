#Juego adivina mi número
import random


numero_secreto = random.randint(1,20)
intentos_restantes = 0
while intentos_restantes < 5:
    intentos_restantes = intentos_restantes + 1
    numero = int(input("Ingresa un numero: "))
    if numero < numero_secreto:
        print("Mi número es mayor")
    if numero > numero_secreto:
        print("Mi número es menor")
    if numero == numero_secreto:
        print("Adivinaste, mi numero era",numero_secreto)
        break

if intentos_restantes == 5:
         if numero != numero_secreto:
          print("No adivinaste, mi número era:",numero_secreto)
         if numero == numero_secreto:
          print("Adivinaste, mi numero era",numero_secreto)