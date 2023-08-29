#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    
    print("¡Bienvenido al juego Adivina mi número!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        try:
            numero = int(input("Ingresa un número: "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue

        if numero < numero_secreto:
            print("Mi número es mayor.")
        elif numero > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
      