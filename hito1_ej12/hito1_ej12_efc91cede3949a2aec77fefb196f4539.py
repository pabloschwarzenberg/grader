"""
15.- Crea un programa para el juego adivina mi número. Tú programa debe comenzar
por generar aleatoriamente un número entre 1 y 20. El jugador tiene 5 intentos para
adivinar el número. En cada intento tu programa debe indicar si el número ingresado
es menor o mayor que el número secreto, imprimiendo el mensaje mi número es menor o mi
número es mayor, según corresponda. Cuando el jugador adivina el número o cuando se superan
los intentos permitidos tu programa debe terminar e indicar al jugador:

•	Si adivinó el número debe decir "Adivinaste, mi número era " e indicar el número secreto.
•	Si no adivinó antes que se acabaran los intentos, tu programa debe decir "No adivinaste,
mi número era " e indicar el número secreto.
"""

import random

numero_aleatorio = random.randint(1, 20)

print("Se ha generado un número al azar! Intenta adivinarlo, tienes 5 intentos:")
for i in range(1, 6):
    print("\n- Intento", i)
    numero = int(input("Número: "))
    if numero < numero_aleatorio:
        print("Mi número es mayor.")
    if numero > numero_aleatorio:
        print("Mi número es menor.")
    if numero == numero_aleatorio:
        print("\nAdivinaste, mi número era", numero_aleatorio)
        break

if numero != numero_aleatorio:
    print("\nNo adivinaste, mi número era", numero_aleatorio)
      