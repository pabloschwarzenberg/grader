#Juego adivina mi número
from os import system
system("cls")

import random

def adivina_mi_numero():
       numero_secreto = random.randint(1, 20)
       intentos = 5
       print("¡Bienvenido al juego Adivina mi número!")
       print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

       while intentos > 0:
        numero = int(input("Ingresa un número: "))
        intentos -= 1
        if numero == numero_secreto:
          print("¡Adivinaste! ¡Mi número era", numero_secreto, "!")
          return
        if numero < numero_secreto:
           print("Mi número es mayor.")
        if numero > numero_secreto:
           print("Mi número es menor.")
           print("¡No adivinaste! Mi número era", numero_secreto)

adivina_mi_numero()      