#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido a 'Adivina mi número'!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        numero_adivinado = int(input("Ingresa tu número: "))

        if numero_adivinado == numero_secreto:
            print("¡Adivinaste, mi número era", numero_secreto, "!")
            return
        elif numero_adivinado < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste, mi número era", numero_secreto, ".")

# Ejecutar el juego
adivina_mi_numero()
     