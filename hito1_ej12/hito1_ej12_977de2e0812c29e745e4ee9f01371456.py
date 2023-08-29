#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a Adivina Mi Número!")
    print("He generado un número secreto entre 1 y 20. ¡Adivina cuál es!")

    while intentos > 0:
        try:
            numero = int(input("Ingresa tu número: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if numero == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif numero < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
      