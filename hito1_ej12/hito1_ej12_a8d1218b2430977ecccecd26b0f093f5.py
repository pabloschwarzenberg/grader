#Juego adivina mi número
import random
intentos = 0
numero_secreto = random.randint(1,20)
print(numero_secreto)
numero = None
while numero_secreto != numero:
     numero = int(input("Adivina mi número secreto (1-20): "))
     if numero > 20:
          print("El número debe de ser entre 1 y 20.")
     if numero > numero_secreto:
          print("Mi numero es menor.")
     elif numero < numero_secreto:
          print("Mi numero es mayor.")
     intentos = intentos + 1
     print(f"Intentos: {intentos}/5")
     if intentos == 5:
          print(f"No adivinaste, mi número era {numero_secreto}")
          break

if numero == numero_secreto:
     print(f"Adivinaste, mi número era {numero_secreto}")
